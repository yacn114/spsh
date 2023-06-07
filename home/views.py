from hesab.models import User
from django.http import HttpResponse
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
    if request.POST:
        siteinformation = informationSite.objects.first()
        language = Languages.objects.filter(status=True)
        category = Category.objects.filter(status=True)
        search_words = request.POST['search']
        searchResualt = Product.objects.filter(name__contains=search_words)
        context = {
            "text":search_words,
            "res":searchResualt,
            "siteData":siteinformation,
            "lang":language,
            "category":category,
        }
        return render(request,"main/searchHome.html",context)
    return render(request,"main/index.html",{
        "product":product,
        "siteData":siteinformation,
        "lang":language,
        "category":category,
        "userc":userCount,
        "prodc":prodc,
        })
def about(request):
    return ""
def error404(request, exception):
    return render(request,"404.html")
def error500(request, exception):
    return render(request,"500.html")