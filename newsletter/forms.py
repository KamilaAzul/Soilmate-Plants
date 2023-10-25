from django import forms
from .models import Subscriber

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='Your Email')

  

        