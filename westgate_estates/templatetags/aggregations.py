from django import template
from westgate_estates.views import *

register = template.Library()

@register.simple_tag
def agg_price(rescom, type, max):
	return get_max_min_price(rescom, type, max)

@register.simple_tag
def agg_bedroom(rescom, type, max):
	return get_max_min_bedroom(rescom, type, max)
