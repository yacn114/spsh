from django.urls import path
from Product.views import detail,detail2,allhot,packages,dislike,like
app_name = "product"
urlpatterns = [
    path('<str:string>',detail,name="detail"),
    path('<int:id>/',detail2,name="detail2"),
    path('packeages/',packages,name="packages"),
    path('hot/',allhot,name="hot"),
    path('like/<int:id>',like,name="like"),
    path('dislike/<int:id>',dislike,name="dislike"),
]
