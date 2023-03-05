from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from category.models import Category,Languages
from home.models import informationSite
from Product.models import Product,teachers
def catWithFilter(request):
    siteData = informationSite.objects.first()

    language = Languages.objects.all()
    category = Category.objects.all()
    teach_count = {}
    pr = Product.objects.filter(published=True)
    teacher = teachers.objects.all()
    for te in teacher:
        co = Product.objects.filter(published=True).filter(teacher_name = te).count()
        teach_count.update({te.name:co})
    pfo = Product.objects.filter(published=True).exclude(price = 0)
    pfc = Product.objects.filter(published=True).filter(price = 0)
    page_obj = 0
    return render(request,"category/full-category.html",{
    
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    "countte":teach_count,
    "pfc":pfc,
    "pfo":pfo,
    "page":page_obj
    })
def categoryList(request,inp):
    
    language = Languages.objects.all()
    category = Category.objects.all()
    cat = get_object_or_404(Category, name=inp)
    pr = Product.objects.filter(published=True)

    siteData = informationSite.objects.first()
    # paginator = Paginator(Product, 1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    page_obj = 0
    return render(request,"category/full-category.html",{
    "inp":cat,
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "page":page_obj
    })