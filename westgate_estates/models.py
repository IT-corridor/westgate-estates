from django.db import models
from autoslug import AutoSlugField

class TRANS_TYPE_ID(models.Model):
    value = models.CharField(max_length=50, unique=True)
    
class STATUS_ID(models.Model):
    value = models.CharField(max_length=50, unique=True)

class PRICE_QUALIFIER(models.Model):
    value = models.CharField(max_length=50, unique=True)

class PROP_SUB_ID(models.Model):
    value = models.CharField(max_length=50, unique=True)

class PUBLISHED_FLAG(models.Model):
    value = models.CharField(max_length=50, unique=True)

class LET_FURN_ID(models.Model):
    value = models.CharField(max_length=50, unique=True)

class LET_RENT_FREQUENCY(models.Model):
    value = models.CharField(max_length=50, unique=True)

class Residential(models.Model):
    AGENT_REF = models.CharField(max_length=12, unique=True)
    SLUG = AutoSlugField(populate_from='AGENT_REF', always_update=True, unique=True)
    ADDRESS_1 = models.CharField(max_length=250)
    ADDRESS_2 = models.CharField(max_length=250)
    ADDRESS_3 = models.CharField(max_length=250)
    ADDRESS_4 = models.CharField(max_length=250)
    TOWN = models.CharField(max_length=60)
    POSTCODE1 = models.CharField(max_length=12)
    POSTCODE2 = models.CharField(max_length=12)
    SUMMARY = models.CharField(max_length=1200)
    DESCRIPTION = models.CharField(max_length=1200)
    BRANCH_ID = models.CharField(max_length=60)
    STATUS_ID = models.ForeignKey(STATUS_ID)
    BEDROOMS = models.CharField(max_length=6)
    PRICE = models.CharField(max_length=12)
    PRICE_QUALIFIER = models.ForeignKey(PRICE_QUALIFIER)
    PROP_SUB_ID = models.ForeignKey(PROP_SUB_ID)
    CREATE_DATE = models.CharField(max_length=20)
    UPDATE_DATE = models.CharField(max_length=20)
    DISPLAY_ADDRESS = models.CharField(max_length=350)
    PUBLISHED_FLAG = models.ForeignKey(PUBLISHED_FLAG)
    LET_DATE_AVAILABLE = models.CharField(max_length=30)
    LET_FURN_ID = models.ForeignKey(LET_FURN_ID)
    LET_RENT_FREQUENCY = models.ForeignKey(LET_RENT_FREQUENCY)
    TRANS_TYPE_ID = models.ForeignKey(TRANS_TYPE_ID)
    MEDIA_IMAGE_00 = models.CharField(max_length=200)
    MEDIA_IMAGE_01 = models.CharField(max_length=200)
    MEDIA_IMAGE_02 = models.CharField(max_length=200)
    MEDIA_IMAGE_03 = models.CharField(max_length=200)
    MEDIA_IMAGE_04 = models.CharField(max_length=200)
    MEDIA_IMAGE_05 = models.CharField(max_length=200)
    MEDIA_IMAGE_06 = models.CharField(max_length=200)
    MEDIA_IMAGE_07 = models.CharField(max_length=200)
    MEDIA_IMAGE_08 = models.CharField(max_length=200)
    MEDIA_IMAGE_09 = models.CharField(max_length=200)
    MEDIA_IMAGE_10 = models.CharField(max_length=200)
    MEDIA_IMAGE_11 = models.CharField(max_length=200)
    MEDIA_IMAGE_12 = models.CharField(max_length=200)
    MEDIA_IMAGE_13 = models.CharField(max_length=200)
    MEDIA_IMAGE_14 = models.CharField(max_length=200)
    MEDIA_IMAGE_15 = models.CharField(max_length=200)
    MEDIA_IMAGE_16 = models.CharField(max_length=200)
    MEDIA_IMAGE_17 = models.CharField(max_length=200)
    MEDIA_IMAGE_18 = models.CharField(max_length=200)
    MEDIA_IMAGE_19 = models.CharField(max_length=200)
    MEDIA_FLOOR_PLAN_00 = models.CharField(max_length=200)
    MEDIA_FLOOR_PLAN_TEXT_00 = models.CharField(max_length=200)
    MEDIA_FLOOR_PLAN_01 = models.CharField(max_length=200)
    MEDIA_FLOOR_PLAN_TEXT_01 = models.CharField(max_length=200)
    MEDIA_IMAGE_60 = models.CharField(max_length=200)
    MEDIA_IMAGE_TEXT_60 = models.CharField(max_length=200)
    MEDIA_IMAGE_61 = models.CharField(max_length=200)
    MEDIA_IMAGE_TEXT_61 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_50 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_50 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_51 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_51 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_52 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_52 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_53 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_53 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_00 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_00 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_01 = models.CharField(max_length=200)
    MEDIA_DOCUMENT_TEXT_01 = models.CharField(max_length=200)
    MEDIA_VIRTUAL_TOUR_01 = models.CharField(max_length=200)
    MEDIA_VIRTUAL_TOUR_TEXT_01 = models.CharField(max_length=200)
    MEDIA_VIRTUAL_TOUR_02 = models.CharField(max_length=200)
    MEDIA_VIRTUAL_TOUR_TEXT_02 = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('residential_property_detail', args=(self.SLUG,))
        
class Commercial(models.Model):
    owner_name = models.CharField(max_length=72)
    owner_address = models.CharField(max_length=250)
    property_address = models.CharField(max_length=250)
    town = models.CharField(max_length=60)
    postcode1 = models.CharField(max_length=12)
    postcode2 = models.CharField(max_length=12)
    summary = models.CharField(max_length=1200)
    description = models.CharField(max_length=1200)
    branch_id = models.CharField(max_length=60)
    status_id = models.CharField(max_length=60)
    bedrooms = models.CharField(max_length=6)
    price = models.CharField(max_length=12)
    price_qualifier = models.CharField(max_length=12)
    prop_sub_id = models.CharField(max_length=20)
    create_date = models.CharField(max_length=20)
    update_date = models.CharField(max_length=20)
    display_address = models.CharField(max_length=350)
    published_flag = models.CharField(max_length=8)
    let_date_available = models.CharField(max_length=30)
    let_furn_id = models.CharField(max_length=50)
    let_rent_frequency = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name