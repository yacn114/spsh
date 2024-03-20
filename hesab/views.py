from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from django.http import HttpResponse
from category.models import Category,Languages
from hesab.forms import ContactForms,completeForm
from .models import Tickets
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
from django.shortcuts import get_object_or_404
@login_required
def ticker(request,id):
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
    value = get_object_or_404(Tickets,id=id)
    
    context = {
        "category":category,
        "siteData":siteData,
        "lang":languagess,
        "value":value,
        }
    
    return render(request,"detail/detail-ticket.html",context)
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
    if request.method == "POST":
        form = completeForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['first_name']
            family = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            githublink = form.cleaned_data['githublink']
            # form.save(update_fields='__all__')
            User.objects.filter(id=request.user.id).update(first_name=name,last_name=family,phone=phone,githublink=githublink)
            messages.success(request, "Done!")
            return redirect("account:home")
    else:
        form = completeForm()
    return render(request,"complete.html",{"Form":completeForm()})
    
