from django.urls import path
from buy.views import bought,Sabad
app_name = "buy"
urlpatterns = [
    path('sabad/<int:id>/',bought, name="bought"),
    path('sabad',Sabad, name="sabad"),

]
