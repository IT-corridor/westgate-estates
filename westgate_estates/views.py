from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Residential
    

def residentiallist(request):
    residentials = Residential.objects.filter(PUBLISHED_FLAG=1, STATUS_ID__in=[0,1,2])
    if request.POST.get('let_furn'):
        price_low = int(request.POST.get('property_price_low'))
        price_high = int(request.POST.get('property_price_high'))
        bedroom_low = int(request.POST.get('property_bedroom_low'))
        bedroom_high = int(request.POST.get('property_bedroom_high'))

        residentials = residentials.filter(PRICE__lte=price_high, PRICE__gte=price_low, BEDROOMS__lte=bedroom_high, BEDROOMS__gte=bedroom_low)

        trans_type = int(request.POST.get('trans_type'))
        price_qualifier = int(request.POST.get('price_qualifier'))
        let_furn = int(request.POST.get('let_furn'))
        let_rent_frequency = int(request.POST.get('let_rent_frequency'))

        if trans_type != -1:
            residentials = residentials.filter(TRANS_TYPE_ID=trans_type)

        if price_qualifier != -1:
            residentials = residentials.filter(PRICE_QUALIFIER=price_qualifier)

        if let_furn != -1:
            residentials = residentials.filter(LET_FURN_ID=let_furn)

        if let_rent_frequency != -1:
            residentials = residentials.filter(LET_RENT_FREQUENCY=let_rent_frequency)

    return render(request, 'residential_property_list.html',
                  {'residentiallist': residentials })


# class ResidentialListView(generic.ListView):

#     # model = Residential
#     template_name = 'residential_property_list.html'
#     #queryset = Residential.objects.filter(publisher__name='Acme Publishing')
#     context_object_name = 'residentiallist'
#     # add filter for TRANS_TYPE_ID

#     def get_queryset(self):
#         """
#         Return the last five published polls (not including those set to be
#         published in the future).
#         """
#         print self.request, '#########'
#         return Residential.objects.all()

    
class ResidentialDetailView(generic.DetailView):

    model = Residential
    template_name = 'residential_property_detail.html'
    slug_field = 'SLUG' # The name of the column that the slug is stored in.
    slug_url_kwarg = 'slug' # The name of the URLConf keyword argument that contains the slug
    context_object_name = 'residentialdetail'
    
#def residential(request):
#    return HttpResponse("Hello, world. You're at the residential propeties index.")


