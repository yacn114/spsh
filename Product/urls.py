from django.urls import path
from Product.views import detail,allhot,packages
app_name = "product"
urlpatterns = [
    path('<str:string>',detail,name="detail"),
    path('packeages/',packages,name="packages"),
    path('hot/',allhot,name="hot"),
]
