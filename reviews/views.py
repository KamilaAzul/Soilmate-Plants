from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import UpdateView, DeleteView
from django.views import View 

from .models import Review, calculate_product_rating
from products.models import Product
from .forms import ReviewForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# Create your views here.


def reviews(request):
    """
    Renders the reviews page with pagination
    """
    reviews_list = Review.objects.filter(approved=True).order_by("-created_at")

    paginate_by = 4
    paginator = Paginator(reviews_list, paginate_by)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'reviews_list': page_obj,
    }

    return render(request, "reviews/all_review.html", context)


class AddReview(View):
    """
    Renders the Add Review page
    """
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ReviewForm()
        return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

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
        return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

class EditReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit User Review
    """
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_review.html'
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


class DeleteReview(DeleteView):
    """
    Delete User Review
    """
    model = Review
    template_name = 'reviews/delete_review.html'
    success_url = reverse_lazy('product_detail')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "The review was deleted successfully")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'product_id': self.object.product.id})