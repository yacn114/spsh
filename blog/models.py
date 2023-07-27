from django.db import models
from hesab.models import User
from category.models import Languages
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateField(auto_now_add=True)
    caption = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Languages)
    image = models.ImageField(upload_to='blog/images')
    
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.name


