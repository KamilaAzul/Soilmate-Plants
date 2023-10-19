from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import BlogPostForm
from .models import Category, Post

# Create your views here.

   
def allBlogPost(request):

    """
    Render the blog page with 9 posts at the time, pagination functionality
    """

    posts = Post.objects.filter(status=1)
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            posts = posts.filter(category=category)

    # Code for sides pagination
    p = Paginator(posts, 9)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)
   

    context = {
        'blog_posts': blog_posts,
        'category': category,
        }

    return render(request, 'blog/all_blog_posts.html', context)


def post_detail(request, slug):
    """
    Renders the post detail Page
    """

    blog_post = get_object_or_404(Post, slug=slug)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_post_detail.html', context)

@login_required
def add_post(request):
    """ This view adds a blog post to the site """

    posts = Post.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'You did not enter any search criteria!')
                return redirect(reverse('home'))
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            posts = posts.filter(queries)

    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            post = form.save()
            messages.success(request, 'Your post was created successfully!')
            return redirect(
                reverse('blog_post_detail', args=[form.instance.slug]))
        else:
            messages.error(request,
                           'Failed to add blog post. '
                           'Please ensure the form is valid.')
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, template, context)
