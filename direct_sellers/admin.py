from django.contrib import admin
from .models import DirectSellerModel

class DirectSellerModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'ref_code', 'earnings_percentage')  # Customize displayed fields

admin.site.register(DirectSellerModel, DirectSellerModelAdmin)
