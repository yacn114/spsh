from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from hesab.forms import ContactForms,completeForm
from .models import Tickets
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
@login_required
def  statusUser(request):

    return render(request,"buy/status-User.html")
@login_required
def complete(request):
    if request.POST:
        return render(request,"complete.html",{"Form":completeForm()})
    else:
        return render(request, '404.html', status=404)

