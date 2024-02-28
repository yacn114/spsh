from hesab.models import User
from Product.models import Product
from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class Transfer_Purchase_history(models.Model):
    CHOICE_TYPE = (
        ('انتقال',"انتقال"),
        ('خرید','خرید'),
    )
    senderـuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+",blank=True,null=True)
    receivingـuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="+",blank=True,null=True)
    amount_send = models.IntegerField(blank=True,null=True)
    user_main = models.ForeignKey(User,on_delete=models.CASCADE,related_name="+")
    user_Pur = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    product_Pur = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    price_Pur = models.IntegerField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    type = models.CharField(max_length=8,choices=CHOICE_TYPE)
    
    class Meta:
        verbose_name = "انتقال و خرید "
        verbose_name_plural = "انتقال و خرید ها"

    def __str__(self):
        return 'object'

