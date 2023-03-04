from django.shortcuts import render
from django.shortcuts import get_object_or_404
from category.models import Category,Languages
from home.models import informationSite
from Product.models import Product,teachers
def categoryList(request,inp):
    teach_count = {}
    pr = Product.objects.filter(published=True)
    teacher = teachers.objects.all()
    for te in teacher:
        co = Product.objects.filter(published=True).filter(teacher_name = te).count()
        teach_count.update({te.name:co})
    language = Languages.objects.all()
    category = Category.objects.all()
    cat = get_object_or_404(Category, name=inp)
    pfc = Product.objects.filter(published=True).filter(price = 0)
    pfo = Product.objects.filter(published=True).exclude(price = 0)
    siteData = informationSite.objects.first()
    return render(request,"category/full-category.html",{
    "inp":cat,
    "category":category,
    "lang":language,
    "siteData":siteData,
    "product":pr,
    "teacher":teacher,
    "countte":teach_count,
    "pfc":pfc,
    "pfo":pfo,
    })