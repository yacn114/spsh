from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from hesab.forms import UserForms,ContactForms
from .models import User,Tickets

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