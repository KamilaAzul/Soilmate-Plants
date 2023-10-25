from . import views
from django.urls import path

urlpatterns = [
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),
]