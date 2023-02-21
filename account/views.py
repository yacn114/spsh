from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import informationSite
@login_required
def home(request):
    return render(request,"account/home.html")

def signup(request):
    pass
def dashboard(request):
    pass
def login(request):
    siteinformation = informationSite.objects.first()

    return render(request,'registration/index.html',{"siteData":siteinformation})
def Forget(request):
    return None