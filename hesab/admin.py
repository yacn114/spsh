from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hesab.models import User,sabad,jamsabad
UserAdmin.fieldsets += (
    ("custom", {"fields":("phone","githublink","prod")}),
    )
UserAdmin.list_display += ('phone','githublink')
admin.site.register(User, UserAdmin)
admin.site.register(sabad)
admin.site.register(jamsabad)