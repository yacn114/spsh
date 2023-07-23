from django.contrib.auth import views
from django.urls import path
from hesab.views import ticket,dashboard,courses,statusUser,response,ticker,complete
app_name = "account"
urlpatterns = [
    path('accounts/complete/',complete,name="complete"),
    path('dashboard/',dashboard,name='home'),
    path('courses/',courses,name='courses'),
    path('ticket/',ticket,name='ticket'),
    path('status/',statusUser,name='status'),
    path('response',response,name='response'),
    path('ticket-datail/<int:id>',ticker,name='ticker'),
    path("logout/", views.LogoutView.as_view(), name="logout"),

]

