from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    LEVEL_NAME = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
    ]
    special_user = models.DateTimeField(default=timezone.now,verbose_name="زمان ویژه")
    name_level = models.CharField(max_length=1,choices=LEVEL_NAME,default='3',verbose_name="سطح کاربر")
    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت اشتراک"