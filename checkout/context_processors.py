from checkout.models import CartItem, Cart
from checkout.views import cart_id
from django.contrib import auth

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    elif auth.user_logged_in:
        try:
            user = auth.get_user(request)
            cart = Cart.objects.filter(user=user.id, is_active=True).first()
            cart_item = CartItem.objects.filter(cart=cart)
            cart_count = cart_item.count
        except Cart.DoesNotExist:
            cart_count = 0
    else:
        cart_count = 0
    return dict(cart_count=cart_count)
