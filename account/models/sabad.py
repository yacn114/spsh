from django.db import models
from account.models import User
from Product.models import Product
class sabad(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    p = models.CharField(max_length=255)
    p2 = models.CharField(max_length=255)
    class Meta:
        verbose_name = "sabad"
        verbose_name_plural = "sabads"

    def __str__(self):
        return str(self.user)


