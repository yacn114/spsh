from django.shortcuts import render,get_object_or_404
from Product.models import Product,Comment
from category.models import Category,Languages
from home.models import informationSite
from django.http import HttpResponse
def detail(request,string):
    Prod = get_object_or_404(Product,slug=string)
    languagess = Languages.objects.all()
    category = Category.objects.all()
    siteData = informationSite.objects.first()
    comment = Comment.objects.filter(user=request.user)
    context ={
        "string":Prod,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "co":comment,
    }
    return render(request,"detail/course-detail.html",context)
def detail2(request,id):
    Prod = get_object_or_404(Product,id=id)
    languagess = Languages.objects.all()
    category = Category.objects.all()
    comment = Comment.objects.filter(user=request.user)
    siteData = informationSite.objects.first()
    context ={
        "string":Prod,
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "co":comment,

    }
    return render(request,"detail/course-detail.html",context)
def allhot(request):
    return HttpResponse("hot tutorials")
def packages(request):
    return HttpResponse("packages")
