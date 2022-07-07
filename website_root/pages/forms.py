from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Your name', 
        widget=forms.TextInput(attrs={
            "class":"form-control"})
    )

    email = forms.EmailField(
        required=False, 
        max_length=100, 
        label='Your e-mail address', 
        widget=forms.TextInput(attrs={
            "class":"form-control"})
    )

    subject = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={"class":"form-control"})
    )

    message = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control", 
        "rows":"5"})
    )
