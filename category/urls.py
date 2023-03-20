from django.urls import path
from category import views
app_name = "category"
urlpatterns = [
    path('category/<str:inp>',views.categoryList,name="category"),
    path('filter/<str:inp>',views.filterCat,name="filterCategory")
]
