from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Category, Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "all_blog_posts.html"
    paginate_by = 9

class PostDetail(View):
    """
    Renders the post detail Page
    """

    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)

        return render(request, 'blog/blog_post_detail.html', {'post': post})

