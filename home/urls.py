from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.ReviewListView.as_view(), name="about"),
    path('contact', views.contact, name="contact"),
    path('design', views.design, name="design"),
    path('thankYou', views.thankYou, name="thankYou"),
]
