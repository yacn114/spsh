from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hesab.models import User
UserAdmin.fieldsets += (
    ("custom", {"fields":("phone","githublink","prod","balance")}),
    )
UserAdmin.list_display += ('phone','githublink',"balance")
admin.site.register(User, UserAdmin)