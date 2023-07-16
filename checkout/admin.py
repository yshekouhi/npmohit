from django.contrib import admin
from .models import Payment, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    # search_fields = ["status",]
    # list_editable = ['status',]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_number', 'first_name','last_name', 'state', 'city', 'status', 'payment_status', 'shipping_status')
    # search_fields = ["status",]
    # list_editable = ['status',]
    list_filter =  ['status', 'payment_status']


    fieldsets = (
        (None, {
            'fields': ('user', ('order_number', 'status', 'payment_status', 'shipping_status'))
        }),
        ('آدرس و مشخصات گیرنده', {
            'fields': ((('state', 'city'), 'shipping_address','zip_code',('first_name','last_name'), ('phone_number','email')))
        })        
    )
    
    inlines = [OrderItemInline,]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_id','status')
    list_editable = ['status',]
    
# admin.site.register(Cart, CartAdmin)
# admin.site.register(CartItem)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

