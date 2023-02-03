from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","hashtag","status","count",)