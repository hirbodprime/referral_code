from django.db.models.signals import pre_save

from .models import Product


def ProductCommissionSignal(sender,instance, **kwargs):
    if not instance.commission1:
        pass

pre_save.connect(ProductCommissionSignal,sender=Product)
