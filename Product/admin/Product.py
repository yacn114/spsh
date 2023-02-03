from django.contrib import admin
from category.models import categories
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title","price","cat","published","view",)
