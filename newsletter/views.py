from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SubscriberForm
from .models import Subscriber, Newsletter
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


class SubscribeView(View):

     def get(self, request):
        form = SubscriberForm()
        return render(request, 'newsletter/subscription_form.html', {'form': form})

     def post(self, request):
        form = SubscriberForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            # Generate a confirmation key
            confirmation_key = get_random_string(length=32)
            form.cleaned_data['confirmation_key'] = confirmation_key

            subscriber = form.save()

            # Send a confirmation email
            send_mail(
                'Confirm Your Subscription',
                f'Thank you for subscribing to our newsletter. To confirm your subscription, click on the following link: {request.build_absolute_uri(f"/confirm/{confirmation_key}/")}',
                'soilmate.plans@gamil.com', 
                [email],
                fail_silently=False,
            )

            return render(request, 'newsletter/subscription_success.html', {'subscriber': subscriber})

        return render(request, 'newsletter/subscription_form.html', {'form': form})


