from django.shortcuts import render
from .models import ProductModel



def products_view(req):
    products = ProductModel.objects.all()
    return render(req,'products/shop.html', {'products':products})





def product_details_view(req, product_name):
    product = ProductModel.objects.get(name=product_name)

    return render(req,'products/shop-description.html',{'p':product})