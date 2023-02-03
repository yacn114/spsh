from django.db import models
from category.models import Category

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
    buyers_count = models.IntegerField("تعداد خریدار")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی ها")
    view = models.IntegerField("تعداد بازدید")
    published = models.BooleanField(default=False,verbose_name="تاریخ انتشار")
    # file = models.FileField()
    count_lesson = models.IntegerField(default=0,verbose_name="تعداد دروس")
    tpye_lang = models.CharField(max_length=50,default="Fa",verbose_name="زبان محصول") # persian or english
    student_count = models.IntegerField(default=1,verbose_name="تعداد دانشجو")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def cat(self):
        return "، ".join([category.name for category in self.category.all()])
    cat.short_description = "دسته‌بندی"

