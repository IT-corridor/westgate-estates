from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
from client.models import *


def residentiallist(request):
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2])
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

    if request.POST.get('let_furn'):
        price_low = int(request.POST.get('property_price_low'))
        price_high = int(request.POST.get('property_price_high'))
        bedroom_low = int(request.POST.get('property_bedroom_low'))
        bedroom_high = int(request.POST.get('property_bedroom_high'))

        residentials = residentials.filter(PRICE__lte=price_high, PRICE__gte=price_low, BEDROOMS__lte=bedroom_high, BEDROOMS__gte=bedroom_low)

        trans_type = int(request.POST.get('trans_type'))
        let_furn = int(request.POST.get('let_furn'))

        if trans_type != -1:
            residentials = residentials.filter(TRANS_TYPE_ID=trans_type)

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
        'save_search':save_search
        })


class ResidentialDetailView(generic.DetailView):

    model = Residential
    template_name = 'residential_property_detail.html'
    slug_field = 'SLUG' # The name of the column that the slug is stored in.
    slug_url_kwarg = 'slug' # The name of the URLConf keyword argument that contains the slug
    context_object_name = 'residentialdetail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ResidentialDetailView, self).get_context_data(**kwargs)        
        context['Let_Rent_Period'] = dict(LET_RENT_FREQUENCY).get(kwargs['object'].LET_RENT_FREQUENCY)

        try:
            save_search = Save_Search.objects.filter(user=self.request.user)
            is_favor = Residential_Favorite.objects.filter(user=self.request.user, residential_id=kwargs['object'].id).exists()
        except Exception, e:
            save_search = None
            is_favor = False

        context['is_favor'] = is_favor

        if save_search:
            save_search = save_search[0]
        context['save_search'] = save_search

        return context


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
    low_price = request.POST.get('property_price_low')
    high_price = request.POST.get('property_price_high')
    low_bedroom = request.POST.get('property_bedroom_low')
    high_bedroom = request.POST.get('property_bedroom_high')
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
        let_furn = request.POST.get('let_furn')
        if let_furn == '-1':
            let_furn = None

        save_search.r_low_price = low_price
        save_search.r_high_price = high_price
        save_search.r_low_bedroom = low_bedroom
        save_search.r_high_bedroom = high_bedroom
        save_search.r_furnished = let_furn
        save_search.save()
    else:
        save_search.s_low_price = low_price
        save_search.s_high_price = high_price
        save_search.s_low_bedroom = low_bedroom
        save_search.s_high_bedroom = high_bedroom
        save_search.save()

    return HttpResponse('success') 