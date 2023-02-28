from django.urls import path
from category import views
app_name = "category"
urlpatterns = [
    path('category/',views.categoryList,name="category"),
]
