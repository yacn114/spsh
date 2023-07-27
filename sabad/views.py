from django.shortcuts import render, redirect
from Product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from home.models import informationSite
from category.models import Languages,Category
@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("sabad:cart_detail")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("sabad:cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("sabad:cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect("sabad:cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("sabad:cart_detail")


@login_required
def cart_detail(request):
    siteData = informationSite.objects.first()
    language = Languages.objects.all()
    category = Category.objects.all()

    return render(request,"buy/sabad.html",{
    "category":category,
    "balance":request.user.balance,
    "lang":language,
    "siteData":siteData,

    })