from django.db import models
from category.models import Languages

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, verbose_name="سلاگ")
    image_preview = models.ImageField(upload_to="images/products", verbose_name="تصویر پیشنمایش")
    tutorial = models.CharField(max_length=100, verbose_name="نوع دوره")
    small_description = models.TextField(verbose_name="توضیح کوتاه")
    long_description = models.TextField(verbose_name="توضیح مفصل")
    price = models.IntegerField(verbose_name="قیمت")
    price_percent = models.IntegerField(verbose_name="درصد تخفیف", default=0)
    hot_price = models.IntegerField(verbose_name="قیمت بگایی تخفیف", default=None, blank=True, null=True)
    language = models.ManyToManyField(Languages,verbose_name="زبان برنامه نویسی")
    view = models.IntegerField("تعداد بازدید")
    published = models.BooleanField(default=False,verbose_name="وضعیت")
    tpye_lang = models.CharField(max_length=50,default="Fa",verbose_name="زبان محصول") # persian or english
    student_count = models.IntegerField(default=1,verbose_name="تعداد دانشجو")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


