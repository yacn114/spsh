from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hesab.models import User,sabad,jamsabad
UserAdmin.fieldsets += (
    ("اشتراک", {"fields":('special_user','name_level',"phone","githublink",)}),
    )
UserAdmin.list_display += ('is_special_user','name_level','phone','githublink',)
admin.site.register(User, UserAdmin)
admin.site.register(sabad)
admin.site.register(jamsabad)