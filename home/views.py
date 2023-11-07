from django.shortcuts import render, redirect
from django.urls import path
from reviews.models import Review
from django.views.generic.edit import FormView
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'home/contact_us.html'

    def form_valid(self, form):
        subject = "New email!"
        message = f"Name: {form.cleaned_data['name']}\nSurname: {form.cleaned_data['surname']}\nEmail: {form.cleaned_data['email']}\nNeed: {form.cleaned_data['need']}\nMessage: {form.cleaned_data['message']}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ["soilmate.plans@gmail.com"]

        send_mail(subject, message, from_email, recipient_list)

        # Add a success message
        messages.success(self.request, "Email was sent successfully!")

        # Redirect to a 'thank you' page
        return redirect(reverse('thank_you'))
          


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









