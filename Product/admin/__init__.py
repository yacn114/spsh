from Product.admin.Product import ProductAdmin
from Product.models import Product,teachers

from django.contrib import admin
admin.site.register(Product, ProductAdmin)
admin.site.register(teachers)

