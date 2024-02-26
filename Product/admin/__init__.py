from Product.admin.Product import ProductAdmin
from Product.models import Product,Comment,IpAddress

from django.contrib import admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(IpAddress)

