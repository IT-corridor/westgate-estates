from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
import re
from westgate_estates.models import *

class Command(BaseCommand):
   
    # !!!!!!!!!!!!!!!!
    # Run command
    # python manage.py importDwellings
    # !!!!!!!!!!!!!!!!
    
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument('--dummy',
                            action='store_true',
                            dest='dummy',
                            default=False,
                            help='Add dummy data instead of data from the .blm file.')
    
    def handle(self, * args, ** options):
        if options['dummy']:
            self.makeTestResidential1()
            self.makeTestResidential2()
        else:
            self.getData()
    
    def getData(self):
        self.stdout.write('Doing stuff...')
        f = open("/home/root/blm_data/WG1.BLM", "r")
        # f = open("/root/WG1.BLM", "r")
        file_contents = f.read()
        buffer = re.split('#[A-Z]+#', file_contents)
        header = buffer[2].strip()
        data = buffer[3].strip()
        dwellings = re.split('~', data)
        
        for dwelling in dwellings:
            #print "\n NEXT ROW \n "
            dwellingData = re.split('\^', dwelling)
            #print ', '.join(dwellingFields) + "\n" + str(len(dwellingFields)) + "---------------------------------------------------------------------"
            if len(dwellingData) == 69:
                # Check to see if residence exists in the database, if so update. If not create.
                if (self.residentialExists(dwellingData)):
                    self.residentailUpdate(dwellingData)
                else:
                    self.makeResidential(dwellingData)
    
    def residentialExists(self, dwellingData):
        if Residential.objects.filter(AGENT_REF=dwellingData[0].strip()).exists():
            return True
        else:
            return False
    
    def residentailUpdate(self, dwellingData):
        print 'Updateing'
        dwelling = Residential.objects.get(AGENT_REF=dwellingData[0].strip())
        dwellingPopulated = self.populateResidential(dwelling, dwellingData)
        dwellingPopulated.save()
    
    def makeResidential(self, dwellingData):
        print 'Create'
        print "\n" + dwellingData[0].strip()  + "//////////////////////////////////////////////////////////" + "\n"
        # dwelling = Residential.objects.create()
        dwelling = Residential()
        dwellingPopulated = self.populateResidential(dwelling, dwellingData)
        dwellingPopulated.save()
    
    def populateResidential(self, dwelling, dwellingData):
        dwelling.AGENT_REF          = dwellingData[0].strip()
        dwelling.ADDRESS_1          = dwellingData[1]
        dwelling.ADDRESS_2          = dwellingData[2]
        dwelling.ADDRESS_3          = dwellingData[3]
        dwelling.ADDRESS_4          = dwellingData[4]
        dwelling.TOWN               = dwellingData[5]
        dwelling.POSTCODE1          = dwellingData[6]
        dwelling.POSTCODE2          = dwellingData[7]
        dwelling.SUMMARY            = dwellingData[8].decode('utf-8', 'replace').replace(u'\ufffd', '')
        dwelling.DESCRIPTION        = dwellingData[9].decode('utf-8', 'replace').replace(u'\ufffd', '')
        dwelling.BRANCH_ID          = dwellingData[10]
        dwelling.STATUS_ID          = int(dwellingData[11])
        dwelling.BEDROOMS           = int(dwellingData[12])
        dwelling.PRICE              = float(dwellingData[13])
        dwelling.PRICE_QUALIFIER    = int(dwellingData[14])
        dwelling.PROP_SUB_ID        = dwellingData[15]
        dwelling.CREATE_DATE        = dwellingData[16]
        dwelling.UPDATE_DATE        = dwellingData[17]
        dwelling.DISPLAY_ADDRESS    = dwellingData[18]
        dwelling.PUBLISHED_FLAG     = int(dwellingData[19])
        dwelling.LET_DATE_AVAILABLE = dwellingData[20]
        dwelling.LET_FURN_ID        = int(dwellingData[21])
        dwelling.LET_RENT_FREQUENCY = int(dwellingData[22])
        dwelling.TRANS_TYPE_ID      = int(dwellingData[23])
        dwelling.MEDIA_IMAGE_00     = dwellingData[24]
        dwelling.MEDIA_IMAGE_01     = dwellingData[25]
        dwelling.MEDIA_IMAGE_02     = dwellingData[26]
        dwelling.MEDIA_IMAGE_03     = dwellingData[27]
        dwelling.MEDIA_IMAGE_04     = dwellingData[28]
        dwelling.MEDIA_IMAGE_05     = dwellingData[29]
        dwelling.MEDIA_IMAGE_06     = dwellingData[30]
        dwelling.MEDIA_IMAGE_07     = dwellingData[31]
        dwelling.MEDIA_IMAGE_08     = dwellingData[32]
        dwelling.MEDIA_IMAGE_09     = dwellingData[33]
        dwelling.MEDIA_IMAGE_10     = dwellingData[34]
        dwelling.MEDIA_IMAGE_11     = dwellingData[35]
        dwelling.MEDIA_IMAGE_12     = dwellingData[36]
        dwelling.MEDIA_IMAGE_13     = dwellingData[37]
        dwelling.MEDIA_IMAGE_14     = dwellingData[38]
        dwelling.MEDIA_IMAGE_15     = dwellingData[39]
        dwelling.MEDIA_IMAGE_16     = dwellingData[40]
        dwelling.MEDIA_IMAGE_17     = dwellingData[41]
        dwelling.MEDIA_IMAGE_18     = dwellingData[42]
        dwelling.MEDIA_IMAGE_19     = dwellingData[43]
        dwelling.MEDIA_FLOOR_PLAN_00        = dwellingData[44]
        dwelling.MEDIA_FLOOR_PLAN_TEXT_00   = dwellingData[45]
        dwelling.MEDIA_FLOOR_PLAN_01        = dwellingData[46]
        dwelling.MEDIA_FLOOR_PLAN_TEXT_01   = dwellingData[47]
        dwelling.MEDIA_IMAGE_60             = dwellingData[48]
        dwelling.MEDIA_IMAGE_TEXT_60        = dwellingData[49]
        dwelling.MEDIA_IMAGE_61             = dwellingData[50]
        dwelling.MEDIA_IMAGE_TEXT_61        = dwellingData[51]
        dwelling.MEDIA_DOCUMENT_50          = dwellingData[52]
        dwelling.MEDIA_DOCUMENT_TEXT_50     = dwellingData[53]
        dwelling.MEDIA_DOCUMENT_51          = dwellingData[54]
        dwelling.MEDIA_DOCUMENT_TEXT_51     = dwellingData[55]
        dwelling.MEDIA_DOCUMENT_52          = dwellingData[56]
        dwelling.MEDIA_DOCUMENT_TEXT_52     = dwellingData[57]
        dwelling.MEDIA_DOCUMENT_53          = dwellingData[58]
        dwelling.MEDIA_DOCUMENT_TEXT_53     = dwellingData[59]
        dwelling.MEDIA_DOCUMENT_00          = dwellingData[60]
        dwelling.MEDIA_DOCUMENT_TEXT_00     = dwellingData[61]
        dwelling.MEDIA_DOCUMENT_01          = dwellingData[62]
        dwelling.MEDIA_DOCUMENT_TEXT_01     = dwellingData[63]
        dwelling.MEDIA_VIRTUAL_TOUR_01      = dwellingData[64]
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_01 = dwellingData[65]
        dwelling.MEDIA_VIRTUAL_TOUR_02      = dwellingData[66]
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_02 = dwellingData[67]
        return dwelling

    def makeTestResidential1(self):

        dwelling = Residential.objects.create()
        dwelling.AGENT_REF = "WG1_1234567"
        dwelling.ADDRESS_1 = "2 Street Street"
        dwelling.ADDRESS_2 = "Wellington Place"
        dwelling.ADDRESS_3 = "Sandwich Industrial Estate"
        dwelling.ADDRESS_4 = ""
        dwelling.TOWN = "Chester"
        dwelling.POSTCODE1 = "CH5"
        dwelling.POSTCODE2 = "1YT"
        dwelling.SUMMARY = "This is a summary."
        dwelling.DESCRIPTION = "A house is a place where lives. They usually have doors and windows. The best kind of house has a cinema room full of cats."
        dwelling.BRANCH_ID = "WG1"
        dwelling.STATUS_ID = "0"
        dwelling.BEDROOMS = 2
        dwelling.PRICE = 555
        dwelling.PRICE_QUALIFIER = 0
        dwelling.PROP_SUB_ID = "26"
        dwelling.CREATE_DATE = "19/09/2015 19:05"
        dwelling.UPDATE_DATE = "19/09/2015 20:55"
        dwelling.DISPLAY_ADDRESS = "2 Street Street"
        dwelling.PUBLISHED_FLAG = 1
        dwelling.LET_DATE_AVAILABLE = "01/11/2015"
        dwelling.LET_FURN_ID = "Unfurnished"
        dwelling.LET_RENT_FREQUENCY = "12 Months"
        dwelling.TRANS_TYPE_ID = "Detached"
        dwelling.MEDIA_IMAGE_00 = "WG1_1234567_IMG_00.JPG"
        dwelling.MEDIA_IMAGE_01 = "WG1_1234567_IMG_01.JPG"
        dwelling.MEDIA_IMAGE_02 = "WG1_1234567_IMG_02.JPG"
        dwelling.MEDIA_IMAGE_03 = ""
        dwelling.MEDIA_IMAGE_04 = ""
        dwelling.MEDIA_IMAGE_05 = ""
        dwelling.MEDIA_IMAGE_06 = ""
        dwelling.MEDIA_IMAGE_07 = ""
        dwelling.MEDIA_IMAGE_08 = ""
        dwelling.MEDIA_IMAGE_09 = ""
        dwelling.MEDIA_IMAGE_10 = ""
        dwelling.MEDIA_IMAGE_11 = ""
        dwelling.MEDIA_IMAGE_12 = ""
        dwelling.MEDIA_IMAGE_13 = ""
        dwelling.MEDIA_IMAGE_14 = ""
        dwelling.MEDIA_IMAGE_15 = ""
        dwelling.MEDIA_IMAGE_16 = ""
        dwelling.MEDIA_IMAGE_17 = ""
        dwelling.MEDIA_IMAGE_18 = ""
        dwelling.MEDIA_IMAGE_19 = ""
        dwelling.MEDIA_FLOOR_PLAN_00 = "WG1_1234567_PLAN_00.JPG"
        dwelling.MEDIA_FLOOR_PLAN_TEXT_00 = "WG1_1234567_PLAN_00.PDF"
        dwelling.MEDIA_FLOOR_PLAN_01 = "WG1_1234567_PLAN_01.JPG"
        dwelling.MEDIA_FLOOR_PLAN_TEXT_01 = "WG1_1234567_PLAN_01.PDF"
        dwelling.MEDIA_IMAGE_60 = ""
        dwelling.MEDIA_IMAGE_TEXT_60 = ""
        dwelling.MEDIA_IMAGE_61 = ""
        dwelling.MEDIA_IMAGE_TEXT_61 = ""
        dwelling.MEDIA_DOCUMENT_50 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_50 = ""
        dwelling.MEDIA_DOCUMENT_51 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_51 = ""
        dwelling.MEDIA_DOCUMENT_52 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_52 = ""
        dwelling.MEDIA_DOCUMENT_53 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_53 = ""
        dwelling.MEDIA_DOCUMENT_00 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_00 = ""
        dwelling.MEDIA_DOCUMENT_01 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_02 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_02 = ""
        dwelling.save()

    def makeTestResidential2(self):

        dwelling = Residential.objects.create()
        dwelling.AGENT_REF = "WG1_765312"
        dwelling.ADDRESS_1 = "Dog Palace"
        dwelling.ADDRESS_2 = "Woofington Road"
        dwelling.ADDRESS_3 = "Boneyard"
        dwelling.ADDRESS_4 = ""
        dwelling.TOWN = "Birmingham"
        dwelling.POSTCODE1 = "B3"
        dwelling.POSTCODE2 = "8UT"
        dwelling.SUMMARY = "This is some summary text."
        dwelling.DESCRIPTION = "A house is a place where people live. They usually have doors and windows. The best kind of house has a dog gym and an iceceam maker."
        dwelling.BRANCH_ID = "B3"
        dwelling.STATUS_ID = "0"
        dwelling.BEDROOMS = "4"
        dwelling.PRICE = "654"
        dwelling.PRICE_QUALIFIER = "0"
        dwelling.PROP_SUB_ID = "28"
        dwelling.CREATE_DATE = "19/09/2015 19:05"
        dwelling.UPDATE_DATE = "19/09/2015 20:55"
        dwelling.DISPLAY_ADDRESS = "Dog Palace"
        dwelling.PUBLISHED_FLAG = "1"
        dwelling.LET_DATE_AVAILABLE = "01/12/2015"
        dwelling.LET_FURN_ID = "Furnished"
        dwelling.LET_RENT_FREQUENCY = "6 Months"
        dwelling.TRANS_TYPE_ID = "Semi-Detached"
        dwelling.MEDIA_IMAGE_00 = "WG1_7654321_IMG_00.JPG"
        dwelling.MEDIA_IMAGE_01 = "WG1_7654321_IMG_01.JPG"
        dwelling.MEDIA_IMAGE_02 = "WG1_7654321_IMG_02.JPG"
        dwelling.MEDIA_IMAGE_03 = ""
        dwelling.MEDIA_IMAGE_04 = ""
        dwelling.MEDIA_IMAGE_05 = ""
        dwelling.MEDIA_IMAGE_06 = ""
        dwelling.MEDIA_IMAGE_07 = ""
        dwelling.MEDIA_IMAGE_08 = ""
        dwelling.MEDIA_IMAGE_09 = ""
        dwelling.MEDIA_IMAGE_10 = ""
        dwelling.MEDIA_IMAGE_11 = ""
        dwelling.MEDIA_IMAGE_12 = ""
        dwelling.MEDIA_IMAGE_13 = ""
        dwelling.MEDIA_IMAGE_14 = ""
        dwelling.MEDIA_IMAGE_15 = ""
        dwelling.MEDIA_IMAGE_16 = ""
        dwelling.MEDIA_IMAGE_17 = ""
        dwelling.MEDIA_IMAGE_18 = ""
        dwelling.MEDIA_IMAGE_19 = ""
        dwelling.MEDIA_FLOOR_PLAN_00 = "WG1_7654321_PLAN_00.JPG"
        dwelling.MEDIA_FLOOR_PLAN_TEXT_00 = "WG1_7654321_PLAN_00.PDF"
        dwelling.MEDIA_FLOOR_PLAN_01 = "WG1_7654321_PLAN_01.JPG"
        dwelling.MEDIA_FLOOR_PLAN_TEXT_01 = "WG1_7654321_PLAN_01.PDF"
        dwelling.MEDIA_IMAGE_60 = ""
        dwelling.MEDIA_IMAGE_TEXT_60 = ""
        dwelling.MEDIA_IMAGE_61 = ""
        dwelling.MEDIA_IMAGE_TEXT_61 = ""
        dwelling.MEDIA_DOCUMENT_50 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_50 = ""
        dwelling.MEDIA_DOCUMENT_51 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_51 = ""
        dwelling.MEDIA_DOCUMENT_52 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_52 = ""
        dwelling.MEDIA_DOCUMENT_53 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_53 = ""
        dwelling.MEDIA_DOCUMENT_00 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_00 = ""
        dwelling.MEDIA_DOCUMENT_01 = ""
        dwelling.MEDIA_DOCUMENT_TEXT_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_01 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_02 = ""
        dwelling.MEDIA_VIRTUAL_TOUR_TEXT_02 = ""
        dwelling.save()
        