import django_filters
from Product.models import Product

A = [
    (0,"رایگان"),
    
    ("","همه"),
]
class ProductFilter(django_filters.FilterSet):
    price = django_filters.ChoiceFilter(choices=A)

    class Meta:
        model = Product
        fields = ["name","price","tutorial_level"]