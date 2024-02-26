from django.urls import path
from buy.views import pay
app_name = "buy"
urlpatterns = [
    path('product_bought/<int:id>/',pay,name="product_bought"),

]
