from django.contrib import admin
from .models import *


class Property_EnquiryAdmin(admin.ModelAdmin):	
	search_fields = ['name', 'enquiry_property__DISPLAY_ADDRESS', 'enquiry_property__SLUG']
	change_list_template = "admin/enquiry_property_change_list.html"

	def changelist_view(self, request, extra_context=None):
		if request.method == 'POST':
			property_id = request.POST.get('property_id')
			conversation = request.POST.get('conversation')
			replied_at = request.POST.get('replied_at_0') + ' ' + request.POST.get('replied_at_1')
			enquiry_property = Property_Enquiry.objects.get(id=int(property_id))
			enquiry_property.conversation = conversation
			enquiry_property.replied_at = replied_at
			enquiry_property.is_replied = True
			enquiry_property.save()

		extra_context = extra_context or {}
		is_replied = request.GET.get('is_replied')
		properties, _ = self.get_search_results(request, Property_Enquiry.objects.all(), request.GET.get('q'))

		if is_replied:
			properties = properties.filter(is_replied=False)

		extra_context['properties'] = properties
		return super(Property_EnquiryAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Property_Enquiry, Property_EnquiryAdmin)

class ResidentialAdmin(admin.ModelAdmin):	
	list_display = ['AGENT_REF', 'RESCOM', 'DISPLAY_ADDRESS', 'TRANS_TYPE_ID', 'STATUS_ID', 'PRICE', 'published']

admin.site.register(Residential, ResidentialAdmin)

class Service_EnquiryAdmin(admin.ModelAdmin):	
	search_fields = ['name', 'enquiry_service__name']
	change_list_template = "admin/enquiry_service_change_list.html"

	def changelist_view(self, request, extra_context=None):
		if request.method == 'POST':
			service_id = request.POST.get('service_id')
			conversation = request.POST.get('conversation')
			replied_at = request.POST.get('replied_at_0') + ' ' + request.POST.get('replied_at_1')
			enquiry_service = Service_Enquiry.objects.get(id=int(service_id))
			enquiry_service.conversation = conversation
			enquiry_service.replied_at = replied_at
			enquiry_service.is_replied = True
			enquiry_service.save()

		extra_context = extra_context or {}
		is_replied = request.GET.get('is_replied')
		services, _ = self.get_search_results(request, Service_Enquiry.objects.all(), request.GET.get('q'))

		if is_replied:
			services = services.filter(is_replied=False)

		extra_context['services'] = services
		return super(Service_EnquiryAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Service_Enquiry, Service_EnquiryAdmin)

class General_EnquiryAdmin(admin.ModelAdmin):	
	search_fields = ['name']
	change_list_template = "admin/enquiry_general_change_list.html"

	def changelist_view(self, request, extra_context=None):
		if request.method == 'POST':
			contact_id = request.POST.get('contact_id')
			conversation = request.POST.get('conversation')
			replied_at = request.POST.get('replied_at_0') + ' ' + request.POST.get('replied_at_1')
			enquiry_contact = General_Enquiry.objects.get(id=int(contact_id))
			enquiry_contact.conversation = conversation
			enquiry_contact.replied_at = replied_at
			enquiry_contact.is_replied = True
			enquiry_contact.save()

		extra_context = extra_context or {}
		is_replied = request.GET.get('is_replied')
		contacts, _ = self.get_search_results(request, General_Enquiry.objects.all(), request.GET.get('q'))

		if is_replied:
			contacts = contacts.filter(is_replied=False)

		extra_context['contacts'] = contacts
		return super(General_EnquiryAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(General_Enquiry, General_EnquiryAdmin)

admin.site.register(Residential_Favorite)
admin.site.register(Save_Search)
