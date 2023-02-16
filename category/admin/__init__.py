from django.contrib import admin
from category.models import Category,Languages
from .Categorya import CategoryAdmin

admin.site.register(Category,CategoryAdmin)
admin.site.register(Languages)