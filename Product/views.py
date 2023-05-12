from django.shortcuts import render,get_object_or_404,redirect
from Product.models import Product,Comment
from category.models import Category,Languages
from home.models import informationSite
from django.http import HttpResponse
def detail(request,string):
    Prod = get_object_or_404(Product,slug=string)
    rec = Product.objects.filter(language=Prod.language.first())
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
        "rec":rec,
    }
    return render(request,"detail/course-detail.html",context)
def detail2(request,id):
    Prod = get_object_or_404(Product,id=id)
    rec = Product.objects.filter(language=Prod.language.first())

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
        "rec":rec,

    }
    return render(request,"detail/course-detail.html",context)
def allhot(request):
    return HttpResponse("hot tutorials")
def packages(request):
    return HttpResponse("packages")

def like(request,id):
    pr = Product.objects.get(id=id)
    lm = Comment.objects.get_or_create(like==request.user,product=pr)
    
    return redirect('/yacn')
def dislike(request,id):
    pass