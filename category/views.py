from django.shortcuts import render
from django.shortcuts import get_object_or_404
from category.models import Category
from home.models import informationSite
from Product.models import Product,teachers
def categoryList(request,inp):
    cat = get_object_or_404(Category, name=inp)
    siteData = informationSite.objects.first()
    pr = Product.objects.all()
    teacher = teachers.objects.all()
    teach_count = {}
    for te in teacher:
        co = Product.objects.filter(teacher_name = te).count()
        teach_count.update({te.name:co})
    return render(request,"main/category.html",{"inp":cat,"siteData":siteData,"product":pr,"teacher":teacher,"countte":teach_count})