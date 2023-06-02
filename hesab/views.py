from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from hesab.forms import UserForms
from .models import User

def signup(request):
    pass

@login_required
def dashboard(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
     
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=request.user.username).update(last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'],githublink=form.cleaned_data['githublink'],first_name=form.cleaned_data['first_name'])

    else:
        form = UserForms()

    return render(request,"account/dash.html",
                  {
                        "form":form,
                        "category":category,
                        "siteData":siteData,
                        "lang":languagess,
                      })
    
def login(request):
    siteinformation = informationSite.objects.first()

    return render(request,'test.html',{"siteData":siteinformation})


@login_required
def Forget(request):
    return None

@login_required
def courses(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
        
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        }
    return render(request,'buy/manage.html',context)
def contact(request):
    return HttpResponse('contact')

def ticket(request):
    pass
def status(request):
    pass