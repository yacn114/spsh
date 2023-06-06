from django.db import models
from hesab.models import User
# Create your models here.
class WalletUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="+")
    balance = models.IntegerField()

    class Meta:
        verbose_name = "ولت"
        verbose_name_plural = "ولت ها"

    def __str__(self):
        return self.user.get_full_name

class historyMoves(models.Model):
    userReceive = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="ارسال کننده",related_name="+")
    userDeposit = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="دریافت کننده",related_name="+")
    date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "تاریخچه انتقال"
        verbose_name_plural = "تاریخچه انتقال ها"

    def __str__(self):
        return self.userDeposit.get_full_name