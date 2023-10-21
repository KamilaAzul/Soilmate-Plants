from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Subscriber.objects.get_or_create(email=email)
            # You can add more logic here, like sending a thank-you email.
            return redirect('thank_you_page')
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribtion_form', {'form': form})
