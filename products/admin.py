from django.contrib import admin
from .models import Product, Category, SpeciesCategory, Light, Size, CareLevel, Safety

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SpeciesCategory)
admin.site.register(Light)
admin.site.register(Size)
admin.site.register(CareLevel)
admin.site.register(Safety)
