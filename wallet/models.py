from hesab.models import User
from Product.models import Product
from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class Transfer(models.Model):
    senderـuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+",blank=True,null=True)
    receivingـuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+",blank=True,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    class Meta:
        verbose_name = "انتقال"
        verbose_name_plural = "انتقال ها"

    def __str__(self):
        return self.senderـuser.username

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "خرید"
        verbose_name_plural = "خرید ها"

    def __str__(self):
        return self.user.username
