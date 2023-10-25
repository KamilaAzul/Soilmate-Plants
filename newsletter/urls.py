from . import views
from django.urls import path

urlpatterns = [
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
    path('confirm/<str:confirmation_code>/', views.ConfirmationView.as_view(), name='confirmation'),
]