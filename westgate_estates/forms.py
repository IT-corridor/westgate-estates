from datetime import date, datetime

from django import forms
from .models import *

class Property_EnquiryForm(forms.ModelForm):
	class Meta:
		model = Property_Enquiry
		fields = ['name', 'email', 'phone', 'enquiry_property', 'contact_email', 'contact_phone', 'message']		
		widgets = {
			'name': forms.TextInput(
				attrs={'required': True}
			),
			'email': forms.TextInput(
				attrs={'required': True}
			),
			'phone': forms.TextInput(
				attrs={'required': True}
			),
			'message': forms.Textarea(
				attrs={'required': True}
			),
			'enquiry_property': forms.HiddenInput(),
		}

class Service_EnquiryForm(forms.ModelForm):
	class Meta:
		model = Service_Enquiry
		fields = ['name', 'email', 'phone', 'enquiry_service', 'contact_email', 'contact_phone', 'message']		
		widgets = {
			'name': forms.TextInput(
				attrs={'required': True}
			),
			'email': forms.TextInput(
				attrs={'required': True}
			),
			'phone': forms.TextInput(
				attrs={'required': True}
			),
			'message': forms.Textarea(
				attrs={'required': True}
			),
			'enquiry_service': forms.HiddenInput(),
		}

class General_EnquiryForm(forms.ModelForm):
	class Meta:
		model = General_Enquiry
		fields = ['name', 'email', 'phone', 'enquiry_text', 'message']		
		widgets = {
			'name': forms.TextInput(
				attrs={'required': True}
			),
			'email': forms.TextInput(
				attrs={'required': True}
			),
			'phone': forms.TextInput(
				attrs={'required': True}
			),
			'message': forms.Textarea(
				attrs={'required': True}
			),
			'enquiry_text': forms.TextInput(
				attrs={'required': True}
			),
		}
