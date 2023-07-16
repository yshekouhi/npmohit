from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from product.models import Product
from .forms import OrderForm, PaymentForm
from .models import Order
from .models import Cart, CartItem, Order, OrderItem, Payment
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings


def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user = request.user, is_active=True)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, cart_id = cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart = cart)
        cart_item.save()

    return redirect('checkout:cart')


@login_required
def increase_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user, is_active=True)
    cart_item = get_object_or_404(CartItem, product=product, cart = cart)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('checkout:cart')


@login_required
def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user, is_active=True)
    cart_item = get_object_or_404(CartItem, product=product, cart = cart)
    cart_item.quantity -= 1
    cart_item.save()

    return redirect('checkout:cart')


@login_required
def remove_from_cart(request, product_id, cart_item_id):
    cart = get_object_or_404(Cart, user = request.user, is_active=True)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('checkout:cart')


@login_required
def cart(request, cart_items = None, total = 0):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(user = request.user, is_active=True)        
        cart_items = CartItem.objects.filter(cart=cart, is_active = True)
        for item in cart_items:
            total += item.product.price * item.quantity
        tax_rate = Decimal(0.09)
        tax = (total*tax_rate)
        tax = Decimal("%.2f" %(tax))
        grand_total = total + tax   
    except ObjectDoesNotExist:
        pass
    context = {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'checkout/cart.html', context)


@login_required
def shipping(request, cart_items = None, total = 0):

    form = OrderForm()

    try:
        cart = Cart.objects.get(user = request.user, is_active=True)        
        cart_items = CartItem.objects.filter(cart=cart, is_active = True)
        for item in cart_items:
            total += item.product.price * item.quantity
        # address = Address.objects.filter(user = request.user).first()
    except ObjectDoesNotExist:
        return HttpResponse('Error')
    context = {
        'cart_items': cart_items,
        'total': total,
        'form': form,
        # 'exist_address': exist_address
    }
    return render(request, 'checkout/shipping.html', context)


@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Calculate total amount (assuming you have a cart or order items logic)
            total_amount = 0  # Your own implementation
            order_number = 0

            # Create the order
            order = Order(
                state=form.cleaned_data['state'],
                city=form.cleaned_data['city'],
                shipping_address=form.cleaned_data['shipping_address'],
                zip_code=form.cleaned_data['zip_code'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                total_amount=total_amount,
                order_number = order_number,
                user = request.user
            )
            order.save()

            # Process the cart items
            cart = Cart.objects.get(user = request.user)  # request.session.get('cart', {})
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                product = Product.objects.get(pk=item.product.id)
                price = product.price * item.quantity
                total_amount += price * item.quantity

                # Create an order item
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    price=price
                )
                order_item.save()

            # Update the total amount of the order
            order.total_amount = total_amount

            # Update the order number of the order
            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime('%Y%m%d')
            order_number = current_date + str(order.id)
            order.order_number = order_number            
            order.save()
            cart.delete()
            # cart.is_active = False
            # cart.save()

            # Redirect to a confirmation page
            # return redirect('order_confirmation', order_id=order.pk)
            return redirect('checkout:orders')
            # return render(request, 'checkout:payment', {'order_id': order.pk})
        else:
            return HttpResponse(form.errors)
    else:
        pass

    return render(request, 'checkout:shipping')

login_required
def payment(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(user=request.user, id=order_id)
        order_number = order.order_number
        image = request.FILES['recipe']
        fs = FileSystemStorage()
        # Generate a new file name

        folder = settings.MEDIA_ROOT/'payment/recipe/'
        
        fs = FileSystemStorage(location=folder)        
        
        new_filename = order_number
        
        # Get the file extension from the original file name
        file_extension = os.path.splitext(image.name)[1]
        # file_extension = os.path.splitext(image)[1]
        
        # Concatenate the new file name and extension
        new_file_path = new_filename + file_extension
        
        # Save the uploaded file with the new file name
        filename = fs.save(new_file_path, image)
        
        # Generate the URL for accessing the uploaded file
        uploaded_file_url = fs.url('payment/recipe/' + filename)        
        payment = Payment(
            user = request.user, 
            order_id = order,
            recipe_image = uploaded_file_url)
        payment.save()
        # return HttpResponse('successpul payment')
        messages.success(request, "اطلاعات پرداخت ثبت شد.")
        return redirect('checkout:orders')
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'checkout/orders.html', {'orders': orders})    

login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'checkout/orders.html', {'orders': orders})

login_required
def cancel(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    order.delete()
    # orders = Order.objects.filter(user=request.user, status='New')
    return redirect('checkout:orders')
    # return render(request, 'checkout/orders.html', {'orders': orders})



def upload_image(request, order_number):
    image = request.FILES['recipe']
    fs = FileSystemStorage()
    # Generate a new file name

    folder = settings.MEDIA_ROOT/'payment/recipe/'
    
    fs = FileSystemStorage(location=folder)        
    
    new_filename = order_number
    
    # Get the file extension from the original file name
    file_extension = os.path.splitext(image.name)[1]
    # file_extension = os.path.splitext(image)[1]
    
    # Concatenate the new file name and extension
    new_file_path = new_filename + file_extension
    
    # Save the uploaded file with the new file name
    filename = fs.save(new_file_path, image)
    
    # Generate the URL for accessing the uploaded file
    uploaded_file_url = fs.url(filename)

    return HttpResponse(uploaded_file_url)
    # return redirect('checkout:orders')
    #     return render(request, 'upload_image.html', {'uploaded_file_url': uploaded_file_url})
    # return render(request, 'upload_image.html')