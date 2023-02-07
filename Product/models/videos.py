from django.db import models
from Product.models import Product
class Video(models.Model):
    id_Product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="آیدی محصول",related_name="+")
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=f"videos/{name}/")


    class Meta:
        verbose_name = "ویدو"
        verbose_name_plural = "ویدو ها"

    def __str__(self):
        return "یه کیر خری حالا انقد گیر نده"
