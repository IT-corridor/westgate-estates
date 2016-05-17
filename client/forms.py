from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    """
    Form for client profile
    """
    phone = forms.RegexField(regex=r'^\d{9,15}$', 
        error_messages = {'invalid': "Phone number must be entered in the format: '999999999'. Up to 15 digits allowed."}, label="Phone Number")

    class Meta:
        model = Client
        fields = ['first_name', 'email', 'email_contactable','phone', 'phone_contactable', 'interested_property','interested_action', 'receive_news', 'interested_service']
        widgets = {
        	'interested_property': forms.CheckboxSelectMultiple,
        	'interested_action': forms.CheckboxSelectMultiple,
        	'interested_service': forms.CheckboxSelectMultiple,
    	}
