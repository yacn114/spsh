from django.db import models

class Languages(models.Model):
    nameE = models.CharField("نام زبان", max_length=50)
    nameF = models.CharField("فارسیش",max_length=50)
    status = models.BooleanField("وضعیت",default=False)
    hashtag = models.CharField("هشتگ انگلیسی", max_length=50)
    category = models.ManyToManyField("category.Category", verbose_name="ذسته بندس ها")
    def __str__(self):
        return self.nameE
    class Meta:
        verbose_name = "زبان برنامه نویسی"
        verbose_name_plural = "زبان ها"
        
