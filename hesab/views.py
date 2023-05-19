from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import informationSite
from category.models import Category,Languages
from hesab.forms import UserForms

def signup(request):
    pass

@login_required
def dashboard(request):
    data = informationSite.objects.first()
    siteData = informationSite.objects.first()
    languagess = Languages.objects.all()
    category = Category.objects.all()
     
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            # ex = Comment()
            # ex.text = form.cleaned_data.get('text')
            # ex.user = request.user
            # ex.product = Product.objects.get(slug=string)
            # ex.save()
            pass
            # return redirect(f"/{string}")
    else:
        form = UserForms()

    return render(request,"account/dash.html",
                  {
                        "form":form,
                        "siteData":data,
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
    return HttpResponse("ok")
def contact(request):
    return HttpResponse('contact')

def ticket(request):
    pass
def status(request):
    pass