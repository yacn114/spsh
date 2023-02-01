from django.contrib import admin
from Product.models import Product

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title",)
