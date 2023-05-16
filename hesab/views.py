from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages

def signup(request):
    pass

@login_required
def dashboard(request):
    data = informationSite.objects.first()
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    return render(request,"account/dash.html",
                  {
                        "siteData":data,
                        "category":category,
                        "siteData":siteData,
                        "lang":languagess,
                      })
    
def login(request):
    siteinformation = informationSite.objects.first()

    return render(request,'registration/index.html',{"siteData":siteinformation})


@login_required
def Forget(request):
    return None

@login_required
def courses(request):
    return HttpResponse("ok")
def contact(request):
    return HttpResponse('contact')