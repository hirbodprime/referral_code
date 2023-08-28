from django.db.models.signals import pre_save
import locale 
import os
from .models import ProductModel


def ProductCommissionSignal(sender,instance, **kwargs):
    if not instance.commission1:
        pass

pre_save.connect(ProductCommissionSignal,sender=ProductModel)




def product_model_price_signal(sender, instance, **kwargs):
    locale.setlocale(locale.LC_ALL, 'en_US')
    
    seprated_price = locale.format("%d", instance.price, grouping=True)
    instance.show_price = seprated_price
    

    
pre_save.connect(product_model_price_signal, sender=ProductModel)