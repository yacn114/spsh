from django.urls import path
from home import views
app_name = "home"

urlpatterns = [
    path('',views.home,name="home"),
    path('about-us',views.about,name="about")
]
