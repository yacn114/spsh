from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    LEVEL_NAME = [
        ('کاربر ویژه','کاربر ویژه'),
        (None,'2'),
        ("کاربر معمولی","کاربر معمولی"),
    ]
    special_user = models.DateTimeField(default=timezone.now,verbose_name="زمان ویژه")
    name_level = models.CharField(max_length=12,choices=LEVEL_NAME,default='3',verbose_name="سطح کاربر")
    profile = models.ImageField(upload_to='profile/',default='profile/profile.png')
    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت اشتراک"
    def is_name_level(self):
        pass
    is_name_level.short_description = "سطح کاربر"