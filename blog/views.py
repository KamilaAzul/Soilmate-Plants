from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .forms import BlogPostForm


# Create your views here.


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 9

class PostDetail(View):
    """
    Renders the post detail Page
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
    
    
        return render(
            request,
            "blog_post_detail.html")