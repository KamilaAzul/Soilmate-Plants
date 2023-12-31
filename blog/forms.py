from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    """
    Form to add a blog post
    """
    class Meta:
        model = Post
        fields = (
            "title",
            "categories",
            "content",
            "featured_image",
        )
