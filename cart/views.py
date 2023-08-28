from django.shortcuts import render, redirect
from .models import CartModel, CartItemModel
from django.contrib.auth.decorators import login_required
from product.models import ProductModel

import locale

@login_required
def view_cart(request):
    cart, created = CartModel.objects.get_or_create(user=request.user)
    items = cart.items.all()

    # Calculate the total bill
    total_bill = sum(item.product.price * item.quantity for item in items)

    # Format the total bill with commas
    locale.setlocale(locale.LC_ALL, 'en_US')  
    formatted_total_bill = locale.format_string("%d", total_bill, grouping=True)

    context = {'cart': cart, 'items': items, 'total_bill': formatted_total_bill}
    return render(request, 'products/cart.html', context)



@login_required
def add_to_cart(request, product_id):
    cart, created = CartModel.objects.get_or_create(user=request.user)
    product = ProductModel.objects.get(id=product_id)
    item, item_created = CartItemModel.objects.get_or_create(user=request.user, product=product)
    if not item_created:
        item.quantity += 1
        item.save()
    cart.items.add(item)
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart = CartModel.objects.get(user=request.user)
    product = ProductModel.objects.get(id=product_id)
    item = CartItemModel.objects.get(user=request.user, product=product)
    item.delete()
    return redirect('cart')

@login_required
def minus_from_cart(request, product_id):
    cart = CartModel.objects.get(user=request.user)
    product = ProductModel.objects.get(id=product_id)
    item = CartItemModel.objects.get(user=request.user, product=product)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')