from django.contrib import admin
from ticket.models import Tickets
class ticketAdmin(admin.ModelAdmin):
    ordering = ("-userdatesend",)
    list_filter = ("subject",)
    list_display = ('user','subject','response')
# Register your models here.

admin.site.register(Tickets,ticketAdmin)