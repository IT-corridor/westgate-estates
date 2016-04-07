from django.contrib import admin
from .models import Residential, Commercial

admin.site.register(Commercial)
admin.site.register(Residential)

