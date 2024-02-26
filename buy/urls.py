from django.urls import path
from buy.views import pay,pay_route
app_name = "buy"
urlpatterns = [
    path('product_bought/<int:id>/',pay,name="product_bought"),
    # path('pay/<int:id>',pay_route,name='pay'),
]
