from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    confirmation_key = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Subscriber
        fields = ['email']
  

        