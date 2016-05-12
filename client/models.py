from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

INTERESTED_ACTION = (
	('Rent', 'Rent'),
	('Buy', 'Buy')
)

INTERESTED_PROPERTIY = (
	('Commercial', 'Commercial'),
	('Residential', 'Residential')
)

OTHER_SERVICE = (
	('Insurance', 'Insurance'),
	('Mortgage', 'Mortgage')
)


class Client(AbstractUser):
    """
    Custom user class
    """
    phone = models.CharField(max_length=50, null=True, blank=True)
    interested_action = models.CharField(choices=INTERESTED_ACTION, max_length=50)
    interested_property = models.CharField(choices=INTERESTED_PROPERTIY, max_length=50)
    other_service = models.CharField(choices=OTHER_SERVICE, max_length=50, default="Insurance")
    receive_news = models.BooleanField(default=False)
    contactable = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username