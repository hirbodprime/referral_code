from django.contrib import admin
from .models import WalletModel

class WalletModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')  # Customize displayed fields

admin.site.register(WalletModel, WalletModelAdmin)
