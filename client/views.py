from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

from .forms import *
from .models import *
from westgate_estates.models import *


@login_required
def profile(request):
	client = Client.objects.get(username=request.user)
	flag = 'create'
	save_search = None
	favorites = None
	residentials = None

	if request.method == 'GET':
		form = ClientForm(initial=model_to_dict(client))		
		
		if client.phone != None:
			flag = 'edit'
			save_search = Save_Search.objects.filter(user=request.user)
	    	if save_search:
	    		save_search = save_search[0]

	        favorites = Residential_Favorite.objects.filter(user=request.user)
	        favorites = [item.residential_id for item in favorites]
	        residentials = Residential.objects.filter(id__in=favorites)

	else:	
		form = ClientForm(request.POST)
		if form.is_valid():			
			client.first_name = form.cleaned_data['first_name']
			client.email = form.cleaned_data['email']
			client.phone = form.cleaned_data['phone']
			client.interested_action = form.cleaned_data['interested_action']
			client.interested_property = form.cleaned_data['interested_property']
			client.interested_service = form.cleaned_data['interested_service']
			client.receive_news = form.cleaned_data['receive_news']
			client.phone_contactable = form.cleaned_data['phone_contactable']
			client.email_contactable = form.cleaned_data['email_contactable']

			client.save()

			return HttpResponseRedirect('/profile/')

	context = {
		'clientform': form,
		'flag': flag,
		'residentiallist': residentials,
		'favorites': favorites,
		'parent_tempate': 'ajax.html',
		'save_search': save_search,
	}

	return render(request, 'profile.html', context)
