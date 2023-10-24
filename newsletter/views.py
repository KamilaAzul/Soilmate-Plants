from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SubscriberForm
from .models import Subscriber, Newsletter
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from mailchimp3 import MailChimp


class SubscribeView(View):

     def post(self, request, *args, **kwargs):
        email = request.POST.get('email')  
        api_key = 'YOUR_MAILCHIMP_API_KEY'
        list_id = 'YOUR_MAILCHIMP_LIST_ID'
        
        if email:
            # Initialize the Mailchimp client
            client = MailChimp(mc_api=api_key, mc_user='your_username')

            # Subscribe the email to your Mailchimp list
            client.lists.members.create_or_update(list_id, {'email_address': email}, merge_fields={'FNAME': 'First Name'})

            # You may want to handle success and error responses here

        return HttpResponseRedirect('newsletter/subscription_success.html') 
           

