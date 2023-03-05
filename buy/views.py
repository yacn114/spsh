from django.shortcuts import render,redirect
from category.models import Category,Languages
from home.models import informationSite
from Product.models import Product,teachers
# Create your views here.
def bought(request,id):
    if request.user.is_authenticated:
        return redirect('/sabad')
    else :
        return redirect('/')
def sabad(request):
    siteData = informationSite.objects.first()
    language = Languages.objects.all()
    category = Category.objects.all()
    pr = Product.objects.filter(published=True)
    teacher = teachers.objects.all()
    return render(request,"buy/manage-course.html",{
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    })