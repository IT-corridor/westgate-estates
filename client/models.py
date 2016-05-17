from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __unicode__(self):
        return self.name


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

    def __unicode__(self):
        return self.username
