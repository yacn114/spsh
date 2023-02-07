from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title","price","cat","published","view",)
