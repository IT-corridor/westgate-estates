from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Residential
    
class ResidentialListView(ListView):

    model = Residential
    template_name = 'residential_property_list.html'
    #queryset = Residential.objects.filter(publisher__name='Acme Publishing')
    context_object_name = 'residentiallist'
    # add filter for TRANS_TYPE_ID
    
class ResidentialDetailView(DetailView):

    model = Residential
    template_name = 'residential_property_detail.html'
    slug_field = 'SLUG' # The name of the column that the slug is stored in.
    slug_url_kwarg = 'slug' # The name of the URLConf keyword argument that contains the slug
    context_object_name = 'residentialdetail'
    
#def residential(request):
#    return HttpResponse("Hello, world. You're at the residential propeties index.")


