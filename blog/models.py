from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model for category
    """

    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


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
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + " | " + str(self.author)