from . import views
from django.urls import path

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletter/', views.newsletter, name="newsletter"),
]