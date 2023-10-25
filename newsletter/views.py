from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SubscriberForm
from .models import Subscriber, Newsletter
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from mailchimp3 import MailChimp
from django.contrib import messages
from requests.exceptions import RequestException
from django.http import JsonResponse, HttpResponse
import os
import requests


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        api_key = os.environ.get('YOUR_MAILCHIMP_API_KEY')
        list_id = os.environ.get('YOUR_LIST_ID')
        endpoint = f'https://usX.api.mailchimp.com/3.0/lists/{list_id}/members'
        data = {
            'email_address': email,
            'status': 'pending',
        }
        headers = {
            'Authorization': f'Bearer {api_key}',
        }
        try:
            response = requests.post(endpoint, json=data, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            if response.status_code == 200:
                # Subscription successful
                # Redirect to subscription success page
                return redirect('subscription_success')
            else:
                return JsonResponse({'message': 'Failed to subscribe. Please ensure the form is valid.'})
        except RequestException as e:
            return JsonResponse({'message': f'Failed to connect to Mailchimp: {str(e)}'})

    return render(request, 'index.html')  # Render the index.html page for GET requests

def subscription_success(request):
    return render(request, 'subscription_success.html')