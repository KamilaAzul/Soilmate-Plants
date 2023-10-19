from django.shortcuts import render

# Create your views here.


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







