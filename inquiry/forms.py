from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'full_name',
            'email',
            'subject',
            'message'
        ]

    subject = forms.CharField(required=False)

    message = forms.CharField(
        required=False,
        widget=forms.Textarea()
    )