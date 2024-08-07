from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from hesab.forms import completeForm
from wallet.models import Transfer_Purchase_history
@login_required
def dashboard(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()

    return render(request,"account/dash.html",
                  {
                    "balance":request.user.balance,
                    "category":category,
                    "siteData":siteData,
                    "lang":languagess,
                      })
@login_required
def courses(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
        
    context = {
        "category":category,
        "balance":request.user.balance,
        "siteData":siteData,
        "lang":languagess,
        }
    return render(request,'buy/manage.html',context)


import json
from django.db.models import Q
@login_required
def  statusUser(request):
    query = Q(user_main=request.user) | Q(receivingـuser=request.user)
    all_history = Transfer_Purchase_history.objects.filter(query)
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    return render(request,"buy/status-User.html",{
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        'data':all_history,
        })
from django.contrib import messages
from hesab.models import User
@login_required
def complete(request):
    if not request.user.first_name:
        if request.method == "POST":
            form = completeForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['first_name']
                family = form.cleaned_data['last_name']
                phone = form.cleaned_data['phone']
                if form.cleaned_data['githublink']:
                    githublink = form.cleaned_data['githublink']
                else:
                    githublink = ""
                User.objects.filter(id=request.user.id).update(first_name=name,last_name=family,phone=phone,githublink=githublink)
                messages.success(request, "Done!")
                return redirect("account:home")
        else:
            form = completeForm()
        return render(request,"complete.html",{"Form":completeForm()})
        
