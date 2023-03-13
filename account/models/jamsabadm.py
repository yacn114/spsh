from django.db import models
from account.models import User
class jamsabad(models.Model):
    jam = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "jam"
        verbose_name_plural = "jam sabad"
    def __str__(self):
        return self.user.name
