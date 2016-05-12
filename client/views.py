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
			post = form.save(commit=False)			
			client.first_name = post.first_name
			client.last_name = post.last_name
			client.email = post.email
			client.phone = post.phone
			client.interested_action = post.interested_action
			client.interested_property = post.interested_property
			client.other_service = post.other_service
			client.receive_news = post.receive_news
			client.contactable = post.contactable

			client.save()
			# # create save_search model for the client for the first time
			# if not Save_Search.objects.filter(user=request.user):
			# 	Save_Search.objects.create(user=request.user)

			return HttpResponseRedirect('/')

	context = {
		'clientform': form,
		'flag': flag,
		'save_search': save_search,
		'favorites': favorites,
		'residentiallist': residentials,
		'parent_tempate': 'ajax.html',
		'save_search': save_search,
	}

	return render(request, 'profile.html', context)
