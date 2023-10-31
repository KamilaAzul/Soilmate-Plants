from django.contrib import admin
from .models import Product, Category, SpeciesCategory, Light, Size, CareLevel, Safety, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'species_category',
        'watering',
        'image',
        'size',
        'safty',
        'care_level',
        'light',
        'price',
        'rating',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SpeciesCategory)
admin.site.register(Light)
admin.site.register(Size)
admin.site.register(CareLevel)
admin.site.register(Safety)

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