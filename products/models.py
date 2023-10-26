from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Modal for categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SpeciesCategory(models.Model):
    """
    Modal for Plant Species categories
    """

    class Meta:
        verbose_name_plural = "Species Categories"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Modal for Product
    """
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    species_category = models.ForeignKey(
        "SpeciesCategory", null=True, blank=True, on_delete=models.SET_NULL
    )
    care_level = models.ForeignKey(
        "CareLevel", null=True, blank=True, on_delete=models.SET_NULL
    )
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size = models.ForeignKey(
        "Size", null=True, blank=True, on_delete=models.SET_NULL
    )
    light = models.ForeignKey(
        "Light", null=True, blank=True, on_delete=models.SET_NULL
    )
    safty = models.ForeignKey(
        "Safety", null=True, blank=True, on_delete=models.SET_NULL
    )
    
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class CareLevel(models.Model):
    """
    Modal for Care level
    """

    class Meta:
        verbose_name_plural = "Care levels"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    """
    Modal for Plants Sizes
    """
    class Meta:
        verbose_name_plural = "Plants Sizes"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
   
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Light(models.Model):
    """
    Modal for Plants exposure to the light
    """
    class Meta:
        verbose_name_plural = "Light exposure"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Safety(models.Model):
    """
    Modal for safety of children and animals
    """
    class Meta:
        verbose_name_plural = "Safety"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Review(models.Model):
    """
    A review for the product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.name}"