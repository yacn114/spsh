from django.db import models
from category.models import Languages,Category


class teachers(models.Model):
    name = models.CharField("اسم مدرس کلیپ",max_length=200)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "مدرس"
        verbose_name_plural = "مدرس ها"

class Product(models.Model):
    LANG= [
        ("Fa","فارسی"),
        ("En","انگلیسی")
    ]
    TYPE_TUTORIAL = [
        ('documnet','documnet'),
        ('video','video'),
        ('short video','short video'),
        ('package','package'),
    ]
    LEVEL_TUTORIAL = [
    ('مبتدی','مبتدی'),
    ('متوسط','متوسط'),
    ('حرفه ای','حرفه ای'),
    ]
    name = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, verbose_name="سلاگ")
    teacher_name = models.ForeignKey(teachers,on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField(upload_to="images/products", verbose_name="تصویر پیشنمایش")
    tutorial = models.CharField(max_length=100, verbose_name="نوع دوره",choices=TYPE_TUTORIAL,default="video")
    tutorial_level = models.CharField(max_length=100, verbose_name="سطح دوره",choices=LEVEL_TUTORIAL,default="junior")
    tutorial_count = models.IntegerField("تعداد ویديو",default=0)
    small_description = models.TextField(verbose_name="توضیح کوتاه")
    long_description = models.TextField(verbose_name="توضیح مفصل")
    price = models.IntegerField(verbose_name="قیمت",default=0)
    pricepercent = models.IntegerField(verbose_name="درصد تخفیف", default=0)
    hot_price = models.IntegerField(verbose_name="قیمت بگایی تخفیف", default=0)
    language = models.ManyToManyField(Languages,verbose_name="زبان برنامه نویسی")
    view = models.IntegerField("تعداد بازدید",default=0)
    tpye_lang = models.CharField(max_length=2,choices=LANG ,default="Fa",verbose_name="زبان محصول") # persian or english
    student_count = models.IntegerField(default=0,verbose_name="تعداد دانشجو")
    published = models.BooleanField(default=True,verbose_name="وضعیت")
    resualt = models.TextField("به چه سطحی میرسه بعد دیدن؟",null=True,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Package(models.Model):
    name = models.CharField(max_length=200)
    tutorials = models.ManyToManyField(Product)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "پکیج"
        verbose_name_plural = "پکیج ها"

    def __str__(self):
        return self.name
