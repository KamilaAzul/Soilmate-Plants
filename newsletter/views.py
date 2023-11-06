from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

from .models import Subscriber
from .forms import SubscriptionForm, NewsletterForm



def subscribe(request):
    """
    Renders the subscription view
    """
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = Subscriber.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = Subscriber()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))
   
@login_required
def account(request):
    if request.user.is_superuser:
        accounts = get_user_model().objects.all()
        # Your logic for the account view

def newsletter(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"PyLessons <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent successfully")
            else:
                messages.error(request, "There was an error sending the email")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = SubscriptionForm()
    form.fields['receivers'].initial = ','.join([active.email for active in Subscriber.objects.all()])
    return render(request=request, template_name='newsletter/newsletter.html', context={'form': form})



