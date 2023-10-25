from django.shortcuts import render, redirect
from django.views import View
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .models import Subscriber
from .forms import SubscriptionForm


class SubscriptionView(View):
    def get(self, request):
        form = SubscriptionForm()
        return render(request, 'newsletter/subscription_form.html', {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            confirmation_code = get_random_string(32)

            subscriber, created = Subscriber.objects.get_or_create(email=email)
            subscriber.is_confirmed = False
            subscriber.save()

            # Send confirmation email
            confirmation_link = f"{request.build_absolute_uri('/')}{confirmation_code}"
            subject = "Confirm Your Subscription"
            message = f"Click the following link to confirm your subscription: {confirmation_link}"
            from_email = "soilmate.plans@gmail.com"  # Update with your email
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return render(request, 'newsletter/subscription_success.html')
        return render(request, 'newsletter/subscription_form.html', {'form': form})


class ConfirmationView(View):
    def get(self, request, confirmation_code):
        try:
            subscriber = Subscriber.objects.get(is_confirmed=False, confirmation_code=confirmation_code)
            subscriber.is_confirmed = True
            subscriber.save()
            return render(request, 'newsletter/subscription_confirmed.html')
        except Subscriber.DoesNotExist:
            messages.error(request, 'Invalid confirmation code!')
            return render(request, 'newsletter/subscription_form.html')

