from django.db import models
from products.models import Product 
from django.db.models import Avg
from django.urls import reverse

# Create your models here.

class Review(models.Model):
    """
    Model for Reviews
    """

    class Meta:
        verbose_name_plural = "Reviews"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    review_title = models.CharField(max_length=100, default='Default Title')
    name = models.CharField(max_length=100, default="Default Name")
    image = models.ImageField(
                              upload_to="review_images",
                              null=True,
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    service_review = models.TextField(null=True, max_length=400)
    service_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse("reviews")
        
def calculate_product_rating(product):
    """ Calculate the average service_rating for the product's reviews"""

    rating = Review.objects.filter(product=product, approved=True).aggregate(Avg('service_rating'))['service_rating__avg']
    return rating if rating is not None else 0 