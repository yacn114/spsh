from django.db import models
from hesab.models import User
class jamsabad(models.Model):
    jam = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "جمع"
        verbose_name_plural = "جمع سبد ها"
    def __str__(self):
        return self.user.username
