from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.ReviewListView.as_view(), name="about"),
    path('design', views.design, name="design"),
    path('thankYou', views.thankYou, name="thankYou"),
    path('contact_view/', views.ContactView.as_view(), name='contact_view'),
]
