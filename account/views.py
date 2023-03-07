from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite

def signup(request):
    pass

@login_required
def dashboard(request):
    data = informationSite.objects.first()
    return render(request,"account/home.html",{"siteData":data})
    
def login(request):
    siteinformation = informationSite.objects.first()

    return render(request,'registration/index.html',{"siteData":siteinformation})


@login_required
def Forget(request):
    return None

@login_required
def courses(request):
    return HttpResponse("ok")