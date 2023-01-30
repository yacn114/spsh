from django.db import models


class Product(models.Model):
    def pathimage(self, slug):
        return "/images/products/" + slug

    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, verbose_name="سلاگ")
    image_preview = models.ImageField(upload_to=pathimage(slug), verbose_name="تصویر پیشنمایش")
    tutorial = models.CharField(max_length=100, verbose_name="نوع دوره")
    small_description = models.TextField(verbose_name="توضیح کوتاه")
    long_description = models.TextField(verbose_name="توضیح مفصل")
    price = models.IntegerField(verbose_name="قیمت")
    price_percent = models.IntegerField(verbose_name="درصد تخفیف", default=0)
    hot_price = models.IntegerField(verbose_name="قیمت بگایی تخفیف", default=None, blank=True, null=True)
    buyers_count = models.IntegerField()
    # category = models.ForeignKey()
    view = models.IntegerField()
    # hashtag = models.ForeignKey()
    # file = models.FileField()
    student_count = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
