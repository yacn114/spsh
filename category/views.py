from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from category.models import Category,Languages
from home.models import informationSite
from Product.models import Product,teachers

def categoryList(request,inp):
    
    languagess = Languages.objects.all()
    category = Category.objects.all()
    cat = get_object_or_404(Languages, hashtag=inp)
    pr = Product.objects.filter(published=True)
    categoryname = Product.objects.filter(published=True).filter(language__hashtag=inp)

    siteData = informationSite.objects.first()
    paginator = Paginator(categoryname, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"category/full-category.html",{
    "inp":cat,
    "category":category,
    "lang":languagess,
    "siteData":siteData,
    "product":pr,
    "page":paginator,
    "categoryname":page_obj,
    })


def filterCat(request,inp):
    languagess = Languages.objects.all()
    category = Category.objects.all()
    cat = get_object_or_404(Languages, nameE=inp)
    siteData = informationSite.objects.first()
    teach_count = {}
    categoryname = Product.objects.filter(published=True).filter(language__nameE=inp)

    pr = Product.objects.filter(published=True)
    teacher = teachers.objects.all()
    for te in teacher:
        co = Product.objects.filter(published=True).filter(teacher_name = te).count()
        teach_count.update({te.name:co})
    pfo = Product.objects.filter(published=True).exclude(price = 0)
    pfc = Product.objects.filter(published=True).filter(price = 0)
    paginator = Paginator(categoryname, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'category/filter-category.html',{
    "inp":cat,
    "category":category,
    "siteData":siteData,
    "lang":languagess,
    "category":category,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    "countte":teach_count,
    "pfc":pfc,
    "pfo":pfo,
    "page":paginator,
    "categoryname":page_obj,
})