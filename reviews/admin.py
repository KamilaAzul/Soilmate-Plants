from django.contrib import admin
from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Displays the Reviews in the admin panel
    """
    list_display = (
        "name",
        "review_title",
        "created_at",
        "service_review",
        "service_rating",
        "approved",
    )