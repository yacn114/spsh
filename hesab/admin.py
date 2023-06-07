from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hesab.models import User,sabad,jamsabad,Tickets
UserAdmin.fieldsets += (
    ("custom", {"fields":("phone","githublink","prod","balance")}),
    )
UserAdmin.list_display += ('phone','githublink',"balance")
admin.site.register(User, UserAdmin)
admin.site.register(sabad)
admin.site.register(Tickets)
admin.site.register(jamsabad)