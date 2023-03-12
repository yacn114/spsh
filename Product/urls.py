from django.urls import path
from Product.views import detail
app_name = "product"
urlpatterns = [
    path('<str:string>',detail,name="detail"),
]
