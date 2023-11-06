from django import forms
from .models import Subscriber
from tinymce.widgets import TinyMCE

class SubscriptionForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

  

        