from django.contrib import admin
from .models import Product, Category, SpeciesCategory, Light, Size, CareLevel, Safety, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'species_category',
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
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'comment')
    list_per_page = 20