from django.contrib.sitemaps import Sitemap

from .models import Residential

class WGSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.5

	def items(self):
		return Residential.objects.all()
