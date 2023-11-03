from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .models import Subscriber
from .forms import SubscriptionForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib import messages
from django.utils.crypto import get_random_string

class SubscriptionView(View):
    """
    Renders the all subscription view
    """
    def post(self, request):
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if not created:
                messages.error(request, _('You are already subscribed.'))
            else:
                subscriber.generate_confirmation_code()
                confirmation_link = reverse('confirmation', args=[subscriber.confirmation_code])
                confirmation_url = f"{get_current_site(request)}{confirmation_link}"
                send_mail(
                    _('Confirm Your Subscription'),
                    f'Please confirm your subscription by clicking on the following link: {confirmation_url}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, _('A confirmation email has been sent to your email address.'))
        else:
            messages.error(request, _('Please provide a valid email address.'))
        return redirect('subscribe')

class ConfirmationView(View):
    """
    Renders the all confirmation view
    """
    def get(self, request, confirmation_code):
        try:
            subscriber = Subscriber.objects.get(confirmation_code=confirmation_code)
            subscriber.confirmation_code = ''
            subscriber.save()
            messages.success(request, _('You have successfully subscribed to our newsletter.'))
        except Subscriber.DoesNotExist:
            messages.error(request, _('Invalid confirmation code.'))
        return redirect('subscribe')

def generate_confirmation_code(email):
    """
    Generate a unique confirmation code based on the email
    """
    
    code = get_random_string(32)
    return code





