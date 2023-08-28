from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, minus_from_cart

urlpatterns = [
    path('', view_cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('minus/<int:product_id>/', minus_from_cart, name='minus_from_cart'),
]
