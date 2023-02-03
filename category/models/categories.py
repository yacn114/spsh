from django.db import models

class Category(models.Model):
    name = models.CharField("اسم دسته بندی", max_length=50)
    created = models.DateField("تاریخ ساخت", auto_now=False, auto_now_add=False)
    hashtag = models.CharField("هشتگ انگلیسی", max_length=50)
    status = models.BooleanField("وضعیت",default=False)
    count = models.IntegerField("تعداد فراخوان",default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        

    