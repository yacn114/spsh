from django.urls import path
from buy.views import bought,sabad
app_name = "buy"
urlpatterns = [
    path('sabad/<int:id>/',bought, name="bought"),
    path('sabad',sabad, name="sabad"),

]
