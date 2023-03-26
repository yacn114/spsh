from django.shortcuts import render,get_object_or_404
from Product.models import Product
from category.models import Category,Languages
from home.models import informationSite
from django.http import HttpResponse
def detail(request,string):
    Prod = get_object_or_404(Product,slug=string)
    languagess = Languages.objects.all()
    category = Category.objects.all()
    siteData = informationSite.objects.first()
    context ={
        "string":Prod,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
 
    }
    return render(request,"detail/detail.html",context)
def allhot(request):
    return HttpResponse("hot tutorials")
def packages(request):
    return HttpResponse("packages")
