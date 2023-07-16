from django.db import models
from account.models import User
from django.utils.translation import gettext as _
from product.models import Product
from enum import Enum


class Cart(models.Model):
    cart_id = models.CharField(_("شناسه"), max_length=50)
    is_active = models.BooleanField(_("فعال؟"), default=True)
    date_added = models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_("کاربر"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        verbose_name_plural = "سبدهای خرید"
        verbose_name = "سبد خرید"    
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name=_("سبد"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("مقدار"))
    is_active = models.BooleanField(_("فعال؟"), default=True)

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name_plural = "اقلام خرید"
        verbose_name = "قلم"  

class PaymentStatus(Enum):
    PENDING= 'در دست بررسی'
    APPROVED = 'تایید شده'
    REJECTED = 'رد شده'

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES  = (
        ('PENDING', 'در دست بررسی'),
        ('APPROVED', 'تایید شده'),
        ('REJECTED', 'رد شده'),
    )       
    user = models.ForeignKey(User, verbose_name=_("کاربر"), on_delete=models.CASCADE)
    order_id = models.ForeignKey("checkout.Order", verbose_name=_("سفارش"), on_delete=models.CASCADE)
    recipe_image = models.ImageField(_("تصویر رسید پرداخت"), upload_to='payment/image', height_field=None, width_field=None, max_length=None) 
    status = models.CharField(_("وضعیت"), max_length=50, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name_plural = "پرداخت‌ها"
        verbose_name = "پرداخت"  

class Order(models.Model):
    ORDER_STATUS_CHOICES  = (
        ('New', 'جدید'),
        ('Accepted', 'پذیرفته شده'),
        ('Completed', 'تکمیل شده'),
        ('Cancelled', 'لغو شده')
    )
    user = models.ForeignKey(User, verbose_name=_("کاربر"), on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(_("شماره سفارش"), max_length=20)
    payment_status = models.BooleanField(_("پرداخت شده"), default=False)
    shipping_status = models.BooleanField(_("ارسال شده"), default=False)
    first_name = models.CharField(_("نام"), max_length=100)
    last_name = models.CharField(_("نام خانوادگی"), max_length=100)
    phone_number = models.CharField(_("تلفن"), max_length=20)
    email = models.EmailField(_("ایمیل"), max_length=254)
    state = models.CharField(_("استان"), max_length=50)
    city = models.CharField(_("شهر"), max_length=100)
    shipping_address = models.TextField(_("آدرس گیرنده"), max_length=100)
    zip_code = models.CharField(_("کد پستی"), max_length=250)
    status = models.BooleanField(_("تایید شده"), max_length=50, default=False)
    total = models.DecimalField(_("جمع کل"), max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(_("پرداخت"), max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ به روزرسانی"), auto_now=True, auto_now_add=False)


    def __str__(self):
        return f"سفارش #{self.pk} - {self.first_name} { self.last_name}"    
    
    class Meta:
        verbose_name_plural = "سفارشات"
        verbose_name = "سفارش"    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("سفارش"), on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name=_("محصول"), on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(_("مقدار"))
    price = models.DecimalField(_("قیمت"), max_digits=10, decimal_places=0)

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name_plural = "اقلام سفارشات"
        verbose_name = "قلم سفارش"  

