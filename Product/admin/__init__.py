from Product.admin.Product import ProductAdmin
from Product.models import Product
from django.contrib import admin
admin.site.register(Product, ProductAdmin)
