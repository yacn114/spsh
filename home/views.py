from django.shortcuts import render
from home.models import informationSite
from Product.models import Product
# Create your views here.
def home(request):
    siteinformation = informationSite.objects.first()
    product = Product.objects.all()
    return render(request,"index.html",{"siteData":siteinformation,"product":product})