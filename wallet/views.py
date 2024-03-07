from wallet.models import Transfer_Purchase_history
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
            user_check = User.objects.filter(username=user_id)
            
            if user_check.exists():
                user = User.objects.get(username=user_id)
                
            else:
                messages.error(request, "نام کاربری وارده اشتباه است !")
                return HttpResponseRedirect(reverse('Wallet:wallet'))
            if request.user.balance >= int(balance):
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
                Transfer_Purchase_history.objects.create(user_main=request.user,senderـuser=request.user,receivingـuser=user,amount_send=balance,type="انتقال")
                return HttpResponseRedirect(reverse('Wallet:wallet'))
            else:
                messages.error(request, "موجودی نداری!")
                return HttpResponseRedirect(reverse('Wallet:wallet'))
    return render(request,"buy/Wallet.html",context)
@login_required
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