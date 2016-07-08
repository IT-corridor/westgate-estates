from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from .models import *
from client.models import *

class WGSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5

	def items(self):
		return Residential.objects.all()

class ServiceSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5

	def items(self):
		return Service_Type.objects.all()

class StaticPagesSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5

	def items(self):
		return ['home', 'contactus']

	def location(self, item):
		return reverse(item)

