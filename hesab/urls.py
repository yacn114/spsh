from django.contrib.auth import views
from django.urls import path
from hesab.views import dashboard,courses,statusUser,complete
app_name = "account"
urlpatterns = [
    path('accounts/complete/',complete,name="complete"),
    path('dashboard/',dashboard,name='home'),
    path('courses/',courses,name='courses'),
    path('status/',statusUser,name='status'),
    path("logout/", views.LogoutView.as_view(), name="logout"),

]

