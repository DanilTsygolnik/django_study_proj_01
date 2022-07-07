from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(required=False, max_length=100, label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
