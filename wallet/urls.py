from django.urls import path
from wallet.views import walletCenter,afzayesh
app_name = "Wallet"
urlpatterns = [
    path("wallet/",walletCenter,name="wallet"),
    path("afzayesh/",afzayesh,name="pay"),
]
