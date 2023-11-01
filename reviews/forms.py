from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("review_title", "service_review", "service_rating", "image")

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )