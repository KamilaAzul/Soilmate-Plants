from django.urls import path
from . import views

urlpatterns = [
   
    path('reviews/<int:product_id>/add_review/', views.AddReview.as_view(), name='add_review'),
    path('reviews/<int:pk>/delete_review/', views.DeleteReview.as_view(), name='delete_review'),
    path('reviews/', views.reviews, name="reviews"),
    path('edit_review/<int:pk>/', views.EditReview.as_view(), name='edit_review'),
]