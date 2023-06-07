from django.shortcuts import render

# Create your views here.
def walletCenter(request):
    context = {
        
    }
    return render(request,"buy/Wallet.html",context)