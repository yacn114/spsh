from django.contrib import admin
from wallet.models import historyMoves,WalletUser
# Register your models here.
admin.site.register(WalletUser)
admin.site.register(historyMoves)