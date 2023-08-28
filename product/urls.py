from django.urls import path 
from .views import products_view, product_details_view

urlpatterns = [
    path('', products_view,name="products"),
    path('detail/<str:product_name>', product_details_view,name="product_details"),

]
