from django.db import models
from hesab.models import User
class Tickets(models.Model):
    subject = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="+")
    message = models.TextField()
    userdatesend = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True,null=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    admindatesend = models.DateTimeField(blank=True,null=True)
        
    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"

    def __str__(self):
        return self.user.username

    