from django.shortcuts import render,get_object_or_404
from Product.models import Product
from django.http import HttpResponse
def detail(request,string):
    a = get_object_or_404(Product,slug=string,published=True)
    return HttpResponse(a)
def allhot(request):
    return HttpResponse("hot tutorials")
def packages(request):
    return HttpResponse("packages")
