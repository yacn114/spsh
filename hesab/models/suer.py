from django.db import models
from django.contrib.auth.models import AbstractUser
from Product.models import Product
class User(AbstractUser):
    prod = models.ManyToManyField(Product,verbose_name="خریداری شذه",blank=True)
    profile = models.ImageField(upload_to='profile/',default='profile/profile.png')
    phone = models.IntegerField(blank=True,null=True)
    githublink = models.CharField(max_length=70,blank=True,null=True)
    balance = models.IntegerField(default=0)
