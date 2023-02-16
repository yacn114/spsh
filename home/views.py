from django.contrib.auth.models import User
from django.shortcuts import render
from home.models import informationSite
from Product.models import Product
from category.models import Languages,Category
# Create your views here.
def home(request):
    siteinformation = informationSite.objects.first()
    product = Product.objects.filter(published=True)
    prodc = Product.objects.filter(published=True).count()
    language = Languages.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    userCount = User.objects.count()
    return render(request,"index.html",{"siteData":siteinformation,"product":product,"lang":language,"userc":userCount,"prodc":prodc,"category":category})