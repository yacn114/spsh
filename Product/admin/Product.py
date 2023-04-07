from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name","price","published","view",)
