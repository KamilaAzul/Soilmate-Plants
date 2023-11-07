from django.shortcuts import render, redirect, reverse
from django.urls import path
from reviews.models import Review
from django.views.generic.edit import FormView
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

          
class ContactView(View):
    template_name = 'home/contact_us.html'  

    def post(self, request):
        # Get form data
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        need = request.POST.get('need')
        message = request.POST.get('message')

        # Send email
        send_mail(
            f'Contact Form Submission from {name} {surname}',
            f'Name: {name}\nSurname: {surname}\nEmail: {email}\nNeed: {need}\nMessage: {message}',
            'soilmate.plans@gmail.com',  
            ['soilmate.plans@gmail.com'],  
            fail_silently=False,
        )

        messages.success(request, 'Email was sent successfully!')

        return redirect('thankYou')

    def get(self, request):
        return render(request, self.template_name)

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









