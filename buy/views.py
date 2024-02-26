# from buy.serializers import buySerializers
# from buy.models import txtmodel
# from django.http import HttpResponse
# from rest_framework import permissionse
from django.contrib.auth.decorators import login_required
# from rest_framework.response import Response
from Product.models import Product
from wallet.models import Purchase
from home.templatetags.price_management import takhfif
from hesab.models import User
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view

# class txtmodelListAPIView(ListAPIView):
 

#     def get_queryset(self):
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         a = txtmodel.objects.first()
#         aa = a.filetxt
#         f = open(str(BASE_DIR) +"/"+ str(aa), "r")
#         # print(f.read())
#         return str(f.read())
        
#     serializer_class = buySerializers
#     permission_classes = [AllowAny]
@api_view(['GET'])
@login_required
def pay(request,id):
    balance = User.objects.get(id=request.user.id)
    prod = Product.objects.get(id=id)
    prcie_pr = takhfif(prod.price,prod.pricepercent,prod.id ,"in")
    for a in balance.prod.all():
        if a.id == prod.id:
            return redirect('product:detail2', id=prod.id)
    if balance.balance >= prcie_pr:
        balance.balance = balance.balance - prcie_pr
        balance.prod.add(prod)
        balance.save()
        Purchase.objects.create(user=balance,product=prod,price=prcie_pr)
        
    else:
        return redirect('Wallet:pay_afzayesh')
    
    return redirect("account:status")


# def show(request):
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     a = txtmodel.objects.first()
#     aa = a.filetxt
#     f = open(str(BASE_DIR) +"/"+ str(aa), "r")
#     return Response(str(f.read()))