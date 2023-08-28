
from django.contrib.auth import get_user_model
from cart.models import CartModel
import locale
User = get_user_model()




def GlobalModels(req):
    if req.user.is_authenticated:
        user = User.objects.get(email=req.user)
        cart, created = CartModel.objects.get_or_create(user=req.user)
        items = cart.items.all()
        # Calculate the total bill
        total_bill = sum(item.product.price * item.quantity for item in items)
        total_items = sum(item.quantity for item in items)
        # Format the total bill with commas
        locale.setlocale(locale.LC_ALL, 'en_US')  
        formatted_total_bill = locale.format_string("%d", total_bill, grouping=True)

        return {
            'user':user,
            'items':items,
            'cart_total_amount':formatted_total_bill,
            'total_items':total_items,
        }
    else:
        return {

        }