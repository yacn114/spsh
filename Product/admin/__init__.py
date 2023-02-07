from Product.admin.Product import ProductAdmin
from Product.admin.videos import VideoAdmin
from Product.models import Product
from Product.models import Video
from django.contrib import admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Video,VideoAdmin)
