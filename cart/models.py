from django.db import models
from product.models import ProductModel

from django.contrib.auth import get_user_model
User = get_user_model()

class CartItemModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CartModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItemModel)
    created_at = models.DateTimeField(auto_now_add=True)
