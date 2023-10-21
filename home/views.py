from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def about(request):
    """
     A view that renders the about page
    """
    return render(request, "home/about_us.html")

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

def subscribe(request):
    """
     A view that renders the Subscription successful page
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Subscribed email: {email}")
        messages.success(request, 'Subscription successful! Thank you for subscribing.')
    return redirect('home') 







