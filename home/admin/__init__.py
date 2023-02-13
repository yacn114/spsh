from django.contrib import admin
from .site import siteAdmin
from home.models import informationSite
admin.site.register(informationSite,siteAdmin)