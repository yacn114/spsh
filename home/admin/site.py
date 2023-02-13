from django.contrib import admin


class siteAdmin(admin.ModelAdmin):
    list_display = ('nameE','nameF')
