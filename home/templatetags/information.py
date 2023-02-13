from home.models import informationSite
from django import template

register = template.Library()

@register.simple_tag
def information(inp):
    if inp == "name":
        return informationSite.objects.all()[0].nameF
    if inp == "nameE":
        return informationSite.objects.all()[0].nameE
    if inp == "logo":
        a = str(informationSite.objects.all()[0].logo)
        return "images/"+a
