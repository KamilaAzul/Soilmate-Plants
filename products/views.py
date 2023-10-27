from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import CreateView, UpdateView
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

class ProductDetail(View):
    template_name = 'products/product_detail.html'

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        reviews = Review.objects.filter(product=product, approved=True)
        form = ReviewForm()
        context = {
            'product': product,
            'reviews': reviews,
            'form': form,
        }
        return render(request, self.template_name, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def reviews(request):
    """
    Renders the reviews page
    """
    reviews_list = Review.objects.filter(approved=True).order_by("-created_at")

    for review in reviews_list:
        review.star_rating = '⭐' * int(review.service_rating)

    context = {
        'reviews_list': reviews_list,
        'can_edit_delete_review': True, 
    }

    return render(request, "products/all_review.html", context)


class AddReview(View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review was sent successfully and is awaiting approval!')
            return redirect('product_detail', product_id=product_id)
        return render(request, 'products/product_detail.html', {'form': form, 'product': product})

class EditReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit User Review
    """
    model = Review
    form_class = ReviewForm
    template_name = "products/edit_review.html"
    success_message = "The review was successfully updated"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and self.request.user != obj.user:
            messages.error(self.request, 'Sorry, only the review creator can edit it.')
            return redirect(reverse('product_detail'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit_delete_review'] = (
            self.request.user.is_authenticated and
            (self.request.user.username == self.object.name or self.request.user.is_superuser)
        )
        return context

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.product.id])

@login_required
def delete_review(request, review_id):
    """
    Delete User Review
    """
    review = get_object_or_404(Review, id=review_id)
    product_id = review.product.id 
    review.delete()
    messages.success(request, "The review was deleted successfully")
    return redirect('product_detail', product_id=product_id)
