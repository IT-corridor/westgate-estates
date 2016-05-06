from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import *
    

def residentiallist(request):
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2])
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

    favorites = Residential_Favorite.objects.all()
    favorites = [item.residential_id for item in favorites]

    return render(request, 'residential_property_list.html',
                  {'residentiallist': residentials, 'favorites': favorites})


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
        context['is_favor'] = Residential_Favorite.objects.filter(residential_id=kwargs['object'].id).exists()
        return context


@csrf_exempt
def update_residential_favorite(request):
    rid = request.POST.get('id')
    operation = request.POST.get('operation')

    if operation == '1':
        Residential_Favorite.objects.create(residential_id=int(rid))
    else:
        Residential_Favorite.objects.get(residential_id=rid).delete()

    return HttpResponse('Your link is invalid or expired!') 

