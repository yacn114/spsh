from django.contrib import admin
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('id_Product',)}