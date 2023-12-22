from django.db import models

# Create your models here.
class txtmodel(models.Model):
    name = models.CharField(max_length=255)
    filetxt = models.FileField("فایل تکست", upload_to="text_files/", max_length=100)



    def __str__(self):
        return self.name
