from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    """
    Form for registering a new client.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True, 'class': 'form-control'}), label="Email Address")
    phone = forms.RegexField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control', 'placeholder': 'Your phone number'}), regex=r'^\d{9,15}$', 
        error_messages = {'invalid': "Phone number must be entered in the format: '999999999'. Up to 15 digits allowed."}, label="Phone Number")

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'interested_action', 'interested_property', 'other_service', 'receive_news', 'contactable']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Your first name'}
            ),
            'last_name': forms.TextInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Your last name'}
            ),
            'interested_action': forms.Select(
                choices=INTERESTED_ACTION,
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Your interested action'}
            ),
            'interested_property': forms.Select(
                choices=INTERESTED_PROPERTIY,
                attrs={'required': True, 'class': 'form-control'}
            ),
            'other_service': forms.Select(
                choices=OTHER_SERVICE, 
                attrs={'class': 'form-control'}
            ),        
            'receive_news': forms.CheckboxInput(
                attrs={'class': 'form-control'}
            ),
            'contactable': forms.CheckboxInput(
                attrs={'class': 'form-control'}
            ),
        }
        labels = {
            'interested_property': '',
        }
