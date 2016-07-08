from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language  

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings
import westgate_estates.views
import client.views
from westgate_estates.sitemaps import WGSitemap

admin.autodiscover()

sitemaps = {
    'properties': WGSitemap()
}

urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url("^admin/", include(admin.site.urls)),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += [
    url('^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    url('^robots\.txt$', include('robots.urls')),

    url("^$", direct_to_template, {"template": "home.html"}, name="home"),
    url('^residential/properties/$', westgate_estates.views.residentiallist, {'rescom': 0}, name='residential_property_list',),
    url('^residential/properties/for-sale/$', westgate_estates.views.residentiallist, {'rescom': 1}, name='residential_property_list_sale',),
    url('^residential/properties/to-rent/$', westgate_estates.views.residentiallist, {'rescom': 2}, name='residential_property_list_rent',),
    url('^commercial/properties/$', westgate_estates.views.residentiallist, {'rescom': 3}, name='commercial_property_list',),
    url('^commercial/properties/for-sale/$', westgate_estates.views.residentiallist, {'rescom': 4}, name='commercial_property_list_sale',),
    url('^commercial/properties/to-rent/$', westgate_estates.views.residentiallist, {'rescom': 5}, name='commercial_property_list_rent',),
    url('^residential/properties/(?P<slug>[-\w]+)/$', westgate_estates.views.property_detail, {'rescom': 0}, name='residential_property_detail'),
    url('^commercial/properties/(?P<slug>[-\w]+)/$', westgate_estates.views.property_detail, {'rescom': 2}, name='commercial_property_detail'),
    url('^services/(?P<slug>[-\w]+)/$', westgate_estates.views.service, name='service'),
    url('^residential/favorite/$', westgate_estates.views.update_residential_favorite, name='update_residential_favorite',),    
    url('^residential/save_search/$', westgate_estates.views.save_search, name='save_search',),        
    url('^contactus/$', westgate_estates.views.contactus, name='contactus',),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', client.views.profile, name='user_profile'),
    url("^", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
