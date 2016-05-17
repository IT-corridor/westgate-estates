from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


TRANS_TYPE_ID = (
    (1, 'Resale'),
    (2, 'Lettings'),
)

STATUS_ID = (
    (0, 'Available'),
    (1, 'SSTC(Sales only)'),
    (2, 'SSTCM(Scottish Sales only'),
    (3, 'Under offer(Sales only'),
    (4, 'Reserved(Sales only'),
    (5, 'Let Agreed(Lettings only')
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

# class PROP_SUB_ID(models.Model):
#     value = models.CharField(max_length=50, unique=True)

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
    MEDIA_IMAGE_00 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_01 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_02 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_03 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_04 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_05 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_06 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_07 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_08 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_09 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_10 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_11 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_12 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_13 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_14 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_15 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_16 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_17 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_18 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_19 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_00 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_TEXT_00 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_01 = models.CharField(max_length=200, blank=True)
    MEDIA_FLOOR_PLAN_TEXT_01 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_60 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_TEXT_60 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_61 = models.CharField(max_length=200, blank=True)
    MEDIA_IMAGE_TEXT_61 = models.CharField(max_length=200, blank=True)
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
    
    def get_absolute_url(self):
        return reverse('residential_property_detail', args=(self.SLUG,))
        
    def __unicode__(self):
        return self.DISPLAY_ADDRESS


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


class Residential_Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    residential = models.ForeignKey(Residential)

    def __unicode__(self):
        return self.user.username+': '+self.residential.DISPLAY_ADDRESS

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
    receive_email = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
