from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    need = forms.ChoiceField(choices=[('invoice', 'Request Invoice for order'),
                                     ('status', 'Request order status'),
                                     ('cashback', "Haven't received cashback yet"),
                                     ('other', 'Other')])
    message = forms.CharField(widget=forms.Textarea)