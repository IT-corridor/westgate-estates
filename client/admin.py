from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mezzanine.core.admin import SitePermissionInline
from .models import *


admin.site.register(Property_Type)
admin.site.register(Action_Type)

class ClientAdmin(UserAdmin):
	fieldsets = None
	fields = ['username', 'password', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'email', 'groups', 'phone', 'email_contactable', 'phone_contactable', 'interested_property', 'interested_action', 'interested_service', 'receive_news']
	list_display = ['name']
	search_fields = ['username', 'first_name', 'last_name', 'email', 'phone']
	list_per_page = 10
	change_list_template = "admin/user_change_list.html"
	inlines = [SitePermissionInline]

	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
		extra_context['clients'], _ = self.get_search_results(request, Client.objects.all(), request.GET.get('q'))
		return super(ClientAdmin, self).changelist_view(request, extra_context=extra_context)


class ServiceAdmin(admin.ModelAdmin):
	change_form_template = 'admin/service_change_form.html'


admin.site.register(Client, ClientAdmin)
admin.site.register(Service_Type, ServiceAdmin)
