from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import informationSite

def signup(request):
    pass

@login_required
def dashboard(request):
    return render(request,"account/home.html")
    
def login(request):
    siteinformation = informationSite.objects.first()

    return render(request,'registration/index.html',{"siteData":siteinformation})
def Forget(request):
    return None