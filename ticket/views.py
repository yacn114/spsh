from django.shortcuts import render,redirect
from home.models import informationSite
from django.contrib.auth.decorators import login_required
from category.models import Category,Languages
from ticket.forms import ContactForms
from .models import Tickets

# Create your views here.
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