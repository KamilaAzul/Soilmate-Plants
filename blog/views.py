from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


from .forms import PostForm
from .models import Category, Post

class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/all_blog_posts.html"
    paginate_by = 9

class PostDetail(View):
    """
    Renders the post detail Page
    """

    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)
    
        return render(request, 'blog/blog_post_detail.html', {'post': post})

def edit_blog_post(request, slug):
        """ This view makes it possible to edit a blog post on the website.
        """

        posts = Post.objects.all()
        query = None

        if not request.user.is_superuser:
            messages.error(request, 'You do not have access to this page!')
            return redirect(reverse('home'))

        blog_post = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            form = PostForm(
                request.POST, request.FILES, instance=blog_post)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.slug = slugify(form.instance.title)
                form.save()
                messages.success(request, 'This post was updated successfully!')
                return redirect(reverse('blog_post_detail', args=[blog_post.slug]))
            else:
                messages.error(request, 'Failed to update blog post. '
                            'Please ensure the form is valid.')
        else:
            form = PostForm(instance=blog_post)
            messages.info(request, f'You are editing the post"{blog_post.title}".')

        template = 'blog/edit_blog_post.html'
        context = {
            'form': form,
            'blog_post': blog_post,
            'posts': posts,
        }
        return render(request, template, context)

@login_required
def create_post(request):
    """
    Creating a new post
    """
    context = {}
    template = "blog/add_blog_post.html"
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n form is valid")
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(
                    request, "Your post was created successfully!")

            return redirect('home')

    context.update({
        'form': form,
        'title': 'Create New Post'
    })
    return render(request, template, context)




    