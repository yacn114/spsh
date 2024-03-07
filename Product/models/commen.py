from django.db import models
from Product.models import Product

class Comment(models.Model):
    user = models.ForeignKey("hesab.User",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField( auto_now_add=True)
    response = models.TextField(blank=True,null=True)
    like = models.ManyToManyField("hesab.User",verbose_name="likes",blank=True,related_name="+")
    dislike = models.ManyToManyField("hesab.User",verbose_name="dislikes",blank=True,related_name="+")
    
    def __str__(self):
        return self.user.username
    
