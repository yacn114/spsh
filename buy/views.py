# from buy.serializers import buySerializers
from buy.models import txtmodel
from Product.models import Product
from home.templatetags.price_management import takhfif
from hesab.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

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
@permission_classes((permissions.AllowAny,))
def pay(request,id):
    balance = User.objects.get(id=request.user.id)
    prod = Product.objects.get(id=id)
    if balance.balance >= takhfif(prod.price,prod.pricepercent,prod.id ,"in"):
        balance.balance = balance.balance - takhfif(prod.price,prod.pricepercent,prod.id ,"in")
        balance.prod.set({prod})
        balance.save()
    else:
        return redirect('Wallet:pay_afzayesh')
    
    return render(request,'buy/pay.html',{"a":balance.balance})
@api_view(['GET'])
def pay_route(request,id):
    pass

# def show(request):
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     a = txtmodel.objects.first()
#     aa = a.filetxt
#     f = open(str(BASE_DIR) +"/"+ str(aa), "r")
#     return Response(str(f.read()))