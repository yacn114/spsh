from django.urls import path
from buy.views import bought,Sabad,delete
app_name = "buy"
urlpatterns = [
    path('sabad/<int:id>/',bought, name="bought"),
    path('sabad',Sabad, name="sabad"),
    path('del/<int:id>',delete, name="delete"),

]
