from django.urls import path
from ticket.views import ticket,response,ticker
app_name = "ticket"
urlpatterns = [
    path('ticket/',ticket,name='ticket'),
    path('response',response,name='response'),
    path('ticket-datail/<int:id>',ticker,name='ticker'),


]
