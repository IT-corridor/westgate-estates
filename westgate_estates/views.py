from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Residential, LET_RENT_FREQUENCY
    

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

    return render(request, 'residential_property_list.html',
                  {'residentiallist': residentials})


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
        return context
