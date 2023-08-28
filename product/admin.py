from django.contrib import admin
from .models import ProductModel



class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','custom_price_name']
    exclude = ('show_price',)
        
    def custom_price_name(self, obj):
        return obj.show_price
    custom_price_name.short_description = 'Price'

admin.site.register(ProductModel,ProductModelAdmin)