from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class Category(models.Model):
    """
    Model for category
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        This meta class orders the model by name.
        """

        ordering = ['name']

    def __str__(self):
        """
        This function returns the name of the category.
        """

        return str(self.name)


CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in CATEGORY_CHOICES:
    choice_list.append(item)


class Post(models.Model):
    """
    Model for the main blog post
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    categories = models.ManyToManyField(Category, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + " | " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()
        

