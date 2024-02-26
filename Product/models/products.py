from django.db import models
from category.models import Languages



class IpAddress(models.Model):
    ips = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)

    class Meta:
        verbose_name = "ip"
        verbose_name_plural = "ips"

    def __str__(self):
        return self.ips


class Product(models.Model):
    LEVEL_TUTORIAL = [
    ('مبتدی','مبتدی'),
    ('متوسط','متوسط'),
    ('حرفه ای','حرفه ای'),
    ]
    name = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, verbose_name="سلاگ")
    image = models.ImageField(upload_to="images/products", verbose_name="تصویر پیشنمایش")
    tutorial = models.CharField(max_length=100, verbose_name="نوع دوره",default="pdf")
    tutorial_level = models.CharField(max_length=100, verbose_name="سطح دوره",choices=LEVEL_TUTORIAL,default="junior")
    small_description = models.TextField(verbose_name="توضیح کوتاه")
    long_description = models.TextField(verbose_name="توضیح مفصل")
    price = models.IntegerField(verbose_name="قیمت",default=0)
    pricepercent = models.IntegerField(verbose_name="درصد تخفیف", default=0)
    hot_price = models.IntegerField(verbose_name="قیمت بگایی تخفیف", default=0)
    language = models.ManyToManyField(Languages,verbose_name="زبان برنامه نویسی")
    student_count = models.IntegerField(default=0,verbose_name="تعداد دانشجو")
    published = models.BooleanField(default=True,verbose_name="وضعیت")
    resualt = models.TextField("به چه سطحی میرسه بعد دیدن؟",null=True,blank=True)
    viewc = models.ManyToManyField(IpAddress,blank=True,related_name="hits")
    def view(self):
        return self.viewc.count()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

