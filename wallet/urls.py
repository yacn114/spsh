from django.urls import path
from wallet.views import walletCenter
app_name = "Wallet"
urlpatterns = [
    path("wallet/",walletCenter,name="wallet")
]
