from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from wallet.forms import WalletMoves
# Create your views here.
@login_required
def walletCenter(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()

    context = {
        "balance":request.user.balance,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "form":WalletMoves,
    }
    return render(request,"buy/Wallet.html",context)
def afzayesh(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
    }
    return render(request,"buy/pay.html",context)