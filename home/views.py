from django.shortcuts import render, redirect
from django.urls import path
from reviews.models import Review
from django.views import generic, View


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def about(request):
    """
     A view that renders the about page
    """
    return render(request, "home/about_us.html")

class ReviewListView(generic.ListView):
    model = Review
    template_name = 'home/about_us.html'  
    context_object_name = 'reviews_list' 
    paginate_by = 3 
    queryset = Review.objects.filter(approved=True).order_by("-created_at")

def contact(request):
    """
     A view that renders the contact page
    """
    return render(request, "home/contact_us.html")

def design(request):
    """
     A view that renders the design page
    """
    return render(request, "home/design.html")

def thankYou(request):
    """
     A view that renders the thank you page
    """
    return render(request, "home/thankYou.html")









