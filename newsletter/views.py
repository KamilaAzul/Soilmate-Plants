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
    template_name = 'subscription_form.html'

    def get(self, request):
        form = SubscriptionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            confirmation_code = generate_confirmation_code(email)
            confirmation_link = f"{request.build_absolute_uri(reverse('confirmation', args=[confirmation_code]))}"
            subject = "Confirm Your Subscription"
            message = f"Click the following link to confirm your subscription: {confirmation_link}"
            from_email = "soilmate.plans@gmail.com"  
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('confirmation', confirmation_code=confirmation_code)
        return render(request, self.template_name, {'form': form})

class ConfirmationView(View):
    """
    Renders the all confirmation view
    """
    def get(self, request, confirmation_code):
        try:
            subscriber = Subscriber.objects.get(is_confirmed=False, confirmation_code=confirmation_code)
            subscriber.is_confirmed = True
            subscriber.save()
            return render(request, 'newsletter/subscription_confirmed.html')
        except Subscriber.DoesNotExist:
            messages.error(request, 'Invalid confirmation code!')
            return render(request, 'newsletter/subscription_form.html')

def generate_confirmation_code(email):
    """
    Generate a unique confirmation code based on the email
    """
    
    code = get_random_string(32)
    return code





