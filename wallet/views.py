from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from wallet.forms import WalletMoves
from django.contrib import messages
from hesab.models import User
# Create your views here.
@login_required
def walletCenter(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()

    context = {
        "balancee":request.user.balance,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "form":WalletMoves,
    }
    if request.method == "POST":
        form = WalletMoves(request.POST)
        if form.is_valid():
            balance = form.cleaned_data['balance']
            user_id = form.cleaned_data['user_id']

            if request.user.balance >= int(balance):
                user= User.objects.get(username=user_id)
                user.balance += int(balance)
                user.save()
                a = User.objects.get(id=request.user.id)
                a.balance = request.user.balance - int(balance)
                a.save()
                context = {
        "balancee":a.balance,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "form":WalletMoves,
    }
                
                messages.success(request, "با موفقیت انتقال داده شد!")
                return HttpResponseRedirect(reverse('Wallet:wallet'))
            else:
                messages.error(request, "موجودی نداری!")
                return HttpResponseRedirect(reverse('Wallet:wallet'))
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