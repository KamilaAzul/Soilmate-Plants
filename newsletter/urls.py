from django.urls import path
from . import views

path('subscribe/', views.subscribe, name="subscribe_form"),
