from home.models import informationSite
from django import template

register = template.Library()

@register.simple_tag
def information(inp):
    if inp == "name":
        return informationSite.objects.all()[0].siteNamePersian
    if inp == "nameE":
        return informationSite.objects.all()[0].siteNameEnglish
    if inp == "logo":
        return str(informationSite.objects.all()[0].logo)

