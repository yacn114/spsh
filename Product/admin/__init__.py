from Product.admin.Product import ProductAdmin
from Product.models import Product,teachers,Comment

from django.contrib import admin
admin.site.register(Product, ProductAdmin)
admin.site.register(teachers)
admin.site.register(Comment)

