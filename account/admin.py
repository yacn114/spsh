from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User
UserAdmin.fieldsets += (
    ("اشتراک", {"fields":('special_user',)}),
    )
UserAdmin.list_display += ('is_special_user',)
admin.site.register(User, UserAdmin)