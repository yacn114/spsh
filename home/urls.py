from django.urls import path
from home import views
from account.views import dashboard
app_name = "home"

urlpatterns = [
    path('',views.home,name="home"),
    path("dashboard/",dashboard,name="dashboard"),
    path('about-us',views.about,name="about")
]
