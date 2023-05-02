from django.urls import path
from buy.views import pay
app_name = "buy"
urlpatterns = [

    path('pay/',pay,name="pay"),
]
