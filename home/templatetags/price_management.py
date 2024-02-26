from django import template
from Product.models import Product
register = template.Library()


@register.simple_tag
def takhfif(price, price_offer,id,call="", *args, **kwargs):
    if price_offer == "0":
        resualt = int(price)
    else:
        resualt = (int(price/100)*int(price_offer)-int(price))*-1
    product = Product.objects.get(id=id)
    if product.hot_price > 0:
        resualt = product.hot_price
    else:
        # resualt = int(price)
        pass
    if call == "in":
        return int(resualt)
    else:
        pass

    return f"{resualt:,}"

@register.simple_tag
def total(items,*args, **kwargs):
    a = 0
    

    for key,value in items:
        v = int(value['product_id'])
        oroduct = Product.objects.get(pk=v)
        a += int((int(value['price'])/100)*int(str(int(oroduct.pricepercent))[0:2])-int(value['price']))*-1

    return f"{a:,}"


@register.simple_tag
def takhfi(price,id,*args, **kwargs):
    pk = int(id)
    a = Product.objects.get(pk=pk)
    res = int((int(price)/100)*int(str(int(a.pricepercent))[0:2])-int(price))*-1
    return f"{res:,}"



@register.simple_tag
def format(resualt,*args, **kwargs):
    res = int(float(resualt))
    return f"{res:,}"
