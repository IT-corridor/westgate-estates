from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Max, Min

import os.path

from .models import *
from client.models import *


def residentiallist(request, rescom):
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2], RESCOM=int(rescom/3))
    trans_type = rescom % 3
    if trans_type > 0:
        residentials = residentials.filter(TRANS_TYPE_ID=trans_type)

    client = Client.objects.filter(username=request.user)
    try:
        save_search = Save_Search.objects.filter(user=request.user)
    except Exception, e:
        save_search = None

    if save_search:
        save_search = save_search[0]

    if request.method == 'GET':
        if client:
            client = client[0]
            # input extra information for a new client
            if client.phone == None:
                return HttpResponseRedirect('/profile/')
    else:
        price_low = int(request.POST.get('property_price_low'))
        price_high = int(request.POST.get('property_price_high'))
        bedroom_low = int(request.POST.get('property_bedroom_low'))
        bedroom_high = int(request.POST.get('property_bedroom_high'))
        let_furn = int(request.POST.get('let_furn') or -1)
        residentials = residentials.filter(PRICE__lte=price_high, PRICE__gte=price_low, BEDROOMS__lte=bedroom_high, BEDROOMS__gte=bedroom_low)

        if let_furn != -1:
            residentials = residentials.filter(LET_FURN_ID=let_furn)

    favorites = []        
    if client:
        favorites = Residential_Favorite.objects.filter(user=request.user)
        favorites = [item.residential_id for item in favorites]

    parent_tempate = "base.html"
    if request.is_ajax():
        parent_tempate = "ajax.html"

    return render(request, 'residential_property_list.html', {
        'residentiallist': residentials, 
        'favorites': favorites, 
        'parent_tempate':parent_tempate, 
        'save_search':save_search,
        'rescom': rescom        
        })


def property_detail(request, slug, rescom):
    prop = Residential.objects.get(SLUG=slug, RESCOM=int(rescom/2))
    images = []
    for i in range(61):
        filename = '/img/properties/%s_IMG_%02d.JPG' % (prop.AGENT_REF.strip(), i)
        if os.path.isfile(settings.STATIC_ROOT+filename):
            images.append(settings.STATIC_URL+filename)
    try:
        save_search = Save_Search.objects.filter(user=self.request.user)
        is_favor = Residential_Favorite.objects.filter(user=self.request.user, residential_id=prop.id).exists()
    except Exception, e:
        save_search = None
        is_favor = False

    if save_search:
        save_search = save_search[0]

    return render(request, 'residential_property_detail.html', {
        'object': prop, 
        'Let_Rent_Period': dict(LET_RENT_FREQUENCY).get(prop.LET_RENT_FREQUENCY),
        'images':images, 
        'is_favor': is_favor,
        'save_search':save_search,
        })


@csrf_exempt
@login_required
def update_residential_favorite(request):
    rid = request.POST.get('id')
    operation = request.POST.get('operation')

    if operation == '1':
        Residential_Favorite.objects.create(user=request.user, residential_id=int(rid))
    else:
        Residential_Favorite.objects.get(user=request.user, residential_id=rid).delete()

    return HttpResponse('success') 

def save_search(request):
    form_id = request.POST.get('form_id')
    print form_id, '@@@@@@@2'
    low_price = request.POST.get('property_price_low')
    high_price = request.POST.get('property_price_high')
    low_bedroom = request.POST.get('property_bedroom_low')
    high_bedroom = request.POST.get('property_bedroom_high')
    let_furn = request.POST.get('let_furn')
    if let_furn == '-1':
        let_furn = None

    receive_email = request.POST.get('receive_email')
    save_search = Save_Search.objects.filter(user=request.user)

    if save_search:
        save_search = save_search[0]
    else:   # create a new one
        save_search = Save_Search(user=request.user)

    save_search.save()

    if receive_email == 'checked':
        save_search.receive_email = True
    elif receive_email == 'unchecked':
        save_search.receive_email = False

    if form_id == 'rent_form':
        save_search.r_low_price = low_price
        save_search.r_high_price = high_price
        save_search.r_low_bedroom = low_bedroom
        save_search.r_high_bedroom = high_bedroom
        save_search.r_furnished = let_furn
        save_search.save()
    elif form_id == 'sale_form':
        save_search.s_low_price = low_price
        save_search.s_high_price = high_price
        save_search.s_low_bedroom = low_bedroom
        save_search.s_high_bedroom = high_bedroom
        save_search.save()
    elif form_id == 'crent_form':
        save_search.cr_low_price = low_price
        save_search.cr_high_price = high_price
        save_search.cr_low_bedroom = low_bedroom
        save_search.cr_high_bedroom = high_bedroom
        save_search.cr_furnished = let_furn
        save_search.save()
    else:
        save_search.cs_low_price = low_price
        save_search.cs_high_price = high_price
        save_search.cs_low_bedroom = low_bedroom
        save_search.cs_high_bedroom = high_bedroom
        save_search.save()

    return HttpResponse('success') 

def get_max_min_price(rescom=0, type=1, max=1):
    '''
    default: get max price for sale properties
    '''
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2], TRANS_TYPE_ID=type, RESCOM=rescom)
    if max:
        result = residentials.aggregate(Max('PRICE'))['PRICE__max'] or 10000
    else:
        result = residentials.aggregate(Min('PRICE'))['PRICE__min'] or 200
    return result

def get_max_min_bedroom(rescom=0, type=1, max=1):
    '''
    default: get max bedroom for sale properties
    '''
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2], TRANS_TYPE_ID=type, RESCOM=rescom)
    if max:
        result = residentials.aggregate(Max('BEDROOMS'))['BEDROOMS__max'] or 7
    else:
        result = residentials.aggregate(Min('BEDROOMS'))['BEDROOMS__min'] or 1
    return result    
