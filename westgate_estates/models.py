from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
import datetime

import client.models

TRANS_TYPE_ID = (
    (1, 'Resale'),      # Sale
    (2, 'Lettings'),    # Rent
)

RES_COM = (
    (0, 'Residential'),      
    (1, 'Commercial'),    
)

STATUS_ID = (
    (0, 'Available'),
    (1, 'SSTC(Sales only)'),
    (2, 'SSTCM(Scottish Sales only)'),
    (3, 'Under offer(Sales only)'),
    (4, 'Reserved(Sales only)'),
    (5, 'Let Agreed(Lettings only)')
)

PRICE_QUALIFIER = (
    (0, 'Default'),
    (1, 'POA'),
    (2, 'Guide Price'),
    (3, 'Fixed Price'),
    (4, 'Offers in Excess'),
    (5, 'OIRO'),
    (6, 'Sales by Tender'),
    (7, 'From(new homes and commercial only)'),
    (9, 'Shared Ownership'),
    (10, 'Offers Over'),
    (11, 'Part Buy Part Rent'),
    (12, 'Shared Equity'),
    (14, 'Equity Loan'),
    (15, 'Offers Invited')    
)

PUBLISHED_FLAG = (
    (0, 'Hidden/invisible'),
    (1, 'Visible'),
)

LET_FURN_ID = (
    (0, 'Furnished'),
    (1, 'Part Furnished'),
    (2, 'Unfurnished'),
    (3, 'Not Specified'),
    (4, 'Furnished/ Un Furnishedf'),
)

LET_RENT_FREQUENCY = (
    (0, 'Weekly'),
    (1, 'Monthly'),
    (2, 'Quarterly'),
    (3, 'Annual'),
    (5, 'Per person per week(Students Lettings only)'),
)


class Residential(models.Model):
    AGENT_REF = models.CharField(max_length=52, unique=True)
    SLUG = AutoSlugField(populate_from='AGENT_REF', always_update=True, unique=True)
    ADDRESS_1 = models.CharField(max_length=250)
    ADDRESS_2 = models.CharField(max_length=250, blank=True)
    ADDRESS_3 = models.CharField(max_length=250, blank=True)
    ADDRESS_4 = models.CharField(max_length=250, blank=True)
    TOWN = models.CharField(max_length=60)
    POSTCODE1 = models.CharField(max_length=52)
    POSTCODE2 = models.CharField(max_length=52)
    SUMMARY = models.TextField()
    DESCRIPTION = models.TextField()
    BRANCH_ID = models.CharField(max_length=60)
    STATUS_ID = models.IntegerField(choices=STATUS_ID, blank=True, null=True)
    BEDROOMS = models.IntegerField(null=True, blank=True)
    PRICE = models.FloatField(null=True, blank=True)
    PRICE_QUALIFIER = models.IntegerField(choices=PRICE_QUALIFIER, blank=True, null=True)
    # PROP_SUB_ID = models.CharField(choices=PROP_SUB_ID, null=True)
    PROP_SUB_ID = models.CharField(max_length=100)
    CREATE_DATE = models.CharField(max_length=20, blank=True)
    UPDATE_DATE = models.CharField(max_length=20, blank=True)
    DISPLAY_ADDRESS = models.CharField(max_length=350)
    PUBLISHED_FLAG = models.IntegerField(choices=PUBLISHED_FLAG, blank=True, null=True)
    LET_DATE_AVAILABLE = models.CharField(max_length=30)
    LET_FURN_ID = models.IntegerField(choices=LET_FURN_ID, blank=True, null=True)
    LET_RENT_FREQUENCY = models.IntegerField(choices=LET_RENT_FREQUENCY, blank=True, null=True)
    TRANS_TYPE_ID = models.IntegerField(choices=TRANS_TYPE_ID, blank=True, null=True)
    MEDIA_IMAGE_00 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_01 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_02 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_03 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_04 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_05 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_06 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_07 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_08 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_09 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_10 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_11 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_12 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_13 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_14 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_15 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_16 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_17 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_18 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_19 = models.FileField(null=True, blank=True)
    MEDIA_FLOOR_PLAN_00 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_TEXT_00 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_01 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_TEXT_01 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_60 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_TEXT_60 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_61 = models.FileField(null=True, blank=True)
    MEDIA_IMAGE_TEXT_61 = models.FileField(null=True, blank=True)
    MEDIA_DOCUMENT_50 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_50 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_51 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_51 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_52 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_52 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_53 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_53 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_00 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_00 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_01 = models.CharField(max_length=200, blank=True)
    MEDIA_DOCUMENT_TEXT_01 = models.CharField(max_length=200, blank=True)
    MEDIA_VIRTUAL_TOUR_01 = models.CharField(max_length=200, blank=True)
    MEDIA_VIRTUAL_TOUR_TEXT_01 = models.CharField(max_length=200, blank=True)
    MEDIA_VIRTUAL_TOUR_02 = models.CharField(max_length=200, blank=True)
    MEDIA_VIRTUAL_TOUR_TEXT_02 = models.CharField(max_length=200, blank=True)
    RESCOM = models.IntegerField(choices=RES_COM, default=0)

    def get_absolute_url(self):
        return reverse('residential_property_detail', args=(self.SLUG,))
        
    def __unicode__(self):
        return self.DISPLAY_ADDRESS

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def published(self):
        return self.PUBLISHED_FLAG
        
    published.boolean = True


class Save_Search(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    r_low_price = models.FloatField(default=100)
    r_high_price = models.FloatField(default=99999)
    r_low_bedroom = models.IntegerField(default=1)
    r_high_bedroom = models.IntegerField(default=12)
    r_furnished = models.IntegerField(choices=LET_FURN_ID, blank=True, null=True)
    s_low_price = models.FloatField(default=100)
    s_high_price = models.FloatField(default=99999)
    s_low_bedroom = models.IntegerField(default=1)
    s_high_bedroom = models.IntegerField(default=12)
    cr_low_price = models.FloatField(default=100)
    cr_high_price = models.FloatField(default=99999)
    cr_low_bedroom = models.IntegerField(default=1)
    cr_high_bedroom = models.IntegerField(default=12)
    cr_furnished = models.IntegerField(choices=LET_FURN_ID, blank=True, null=True)
    cs_low_price = models.FloatField(default=100)
    cs_high_price = models.FloatField(default=99999)
    cs_low_bedroom = models.IntegerField(default=1)
    cs_high_bedroom = models.IntegerField(default=12)
    receive_email = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Saved Search'
        verbose_name_plural = 'Saved Searches'

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Property_Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    enquiry_property = models.ForeignKey(Residential, null=True)
    contact_email = models.BooleanField(default=True)
    contact_phone = models.BooleanField(default=True)
    message = models.TextField(blank=True, null=True)
    conversation = models.TextField(default='Not yet replied')
    created_at = models.DateTimeField(auto_now=True)
    replied_at = models.DateTimeField(null=True)
    is_replied = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Property Enquiries'

    def date_replied(self):
        if self.is_replied:
            return self.replied_at.strftime('%d/%m/%y %H:%M')
        return 'Not yet replied'

    def get_user(self):
        return client.models.Client.objects.get(email=self.email).id

    def __unicode__(self):
        return self.name


class Service_Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    enquiry_service = models.ForeignKey(client.models.Service_Type, null=True)
    contact_email = models.BooleanField(default=True)
    contact_phone = models.BooleanField(default=True)
    message = models.TextField(blank=True, null=True)
    conversation = models.TextField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now=True)
    replied_at = models.DateTimeField(null=True)
    is_replied = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Service Enquiry'
        verbose_name_plural = 'Service Enquiries'

    def date_replied(self):
        if self.is_replied:
            return self.replied_at.strftime('%d/%m/%y %H:%M')
        return 'Not yet replied'

    def get_user(self):
        return client.models.Client.objects.get(email=self.email).id

    def __unicode__(self):
        return self.name


class General_Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    enquiry_text = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.BooleanField(default=True)
    contact_phone = models.BooleanField(default=True)
    message = models.TextField(blank=True, null=True)
    conversation = models.TextField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now=True)
    replied_at = models.DateTimeField(null=True)
    is_replied = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'

    def date_replied(self):
        if self.is_replied:
            return self.replied_at.strftime('%d/%m/%y %H:%M')
        return 'Not yet replied'

    def get_user(self):
        return client.models.Client.objects.get(email=self.email).id
        
    def __unicode__(self):
        return self.name


class Residential_Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    residential = models.ForeignKey(Residential)

    def __unicode__(self):
        return self.user.username+': '+self.residential.DISPLAY_ADDRESS
