from django.contrib import admin
from .models import PurchaseModel

class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')  # Customize displayed fields

admin.site.register(PurchaseModel, PurchaseModelAdmin)
