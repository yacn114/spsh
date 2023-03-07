from django.shortcuts import render,redirect
from category.models import Category,Languages
from home.models import informationSite
from django.contrib.auth.decorators import login_required
from Product.models import teachers
from account.models import sabad
# Create your views here.
@login_required
def bought(request,id):
    return redirect('/sabad')

@login_required
def Sabad(request):
    siteData = informationSite.objects.first()
    language = Languages.objects.all()
    category = Category.objects.all()
    pr = sabad.objects.filter(user__username=request.user.username)
    teacher = teachers.objects.all()
    return render(request,"buy/manage-course.html",{
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    })