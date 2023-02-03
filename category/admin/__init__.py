from django.contrib import admin
from category.models import Category
from .Categorya import CategoryAdmin

admin.site.register(Category,CategoryAdmin)