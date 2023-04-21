from django.db import models
from hesab.models import User
from Product.models import Product
class sabad(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    p = models.IntegerField(default=0)
    p2 = models.IntegerField(default=0)
    class Meta:
        verbose_name = "سبد"
        verbose_name_plural = "سبد ها"

    def __str__(self):
        return str(self.user)


