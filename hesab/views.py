from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from django.http import HttpResponse
from category.models import Category,Languages
from hesab.forms import ContactForms,completeForm
from .models import Tickets
from wallet.models import Purchase,Transfer
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
@login_required
def ticket(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "form":ContactForms(),
        }
    if request.POST:
        ti = Tickets()
        text = request.POST['text']
        user = request.user
        ti.message = text
        ti.user = user
        ti.subject = request.POST.get('subject')
        ti.save()
        return redirect('/response')
    else:
        ContactForms()

    return render(request,'detail/contact.html',context)
@login_required
def response(request):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    ti = Tickets.objects.filter(user=request.user)
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "ti":ti,
        "balance":request.user.balance,
        }
    return render(request,"detail/responses.html",context)
@login_required
def ticker(request,id):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    value = Tickets.objects.get(id=id)
    
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "value":value,
        }
    
    return render(request,"detail/detail-ticket.html",context)
import json
@login_required
def  statusUser(request):
    data_purchase = Purchase.objects.filter(user=request.user)
    data_transfer = Transfer.objects.filter(senderـuser=request.user)
    data_combined = data_purchase.union(data_transfer).order_by('date')
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    return render(request,"buy/status-User.html",{
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        'data':data_combined,
        })
    

@login_required
def complete(request):
    if request.POST:
        return render(request,"complete.html",{"Form":completeForm()})
    else:
        return render(request, '404.html', status=404)

