from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

import westgate_estates.models

class Property_Type(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Action_Type(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Service_Type(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Client(AbstractUser):
    """
    Custom user class
    """
    email_contactable = models.BooleanField(default=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    phone_contactable = models.BooleanField(default=True)    
    interested_property = models.ManyToManyField(Property_Type, related_name="property")
    interested_action = models.ManyToManyField(Action_Type, related_name="action")
    interested_service = models.ManyToManyField(Service_Type, related_name="service")
    receive_news = models.BooleanField(default=True)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def favorite_properties(self):
        favorites = westgate_estates.models.Residential_Favorite.objects.filter(user=self.id)
        properties = [item.residential.id for item in favorites]            
        properties = westgate_estates.models.Residential.objects.filter(id__in=properties)
        return [item.SLUG for item in properties]

    def services_in_profile(self):
        services = self.interested_service.all()
        services = [item.name for item in services]
        return ','.join(services);

    def properties_enquiries(self):
        contacts = westgate_estates.models.Property_Enquiry.objects.filter(email=self.email)        
        return [item.enquiry_property.SLUG for item in contacts]            

    def services_enquiries(self):
        contacts = westgate_estates.models.Service_Enquiry.objects.filter(email=self.email)        
        return [item.enquiry_service.name for item in contacts]            

    def is_contacted(self):
        return westgate_estates.models.General_Enquiry.objects.filter(email=self.email)        

    def __unicode__(self):
        return self.username

