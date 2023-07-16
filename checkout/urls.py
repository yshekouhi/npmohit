from django.urls import path
from . import views

app_name = 'checkout'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path("shipping/", views.shipping, name="shipping"),
    path("place_order/", views.place_order, name="place_order"),
    path("orders/", views.orders, name="orders"),
    path("orders/cancel/<int:order_id>", views.cancel, name="cancel"),
    path("payment/<int:order_id>", views.payment, name="payment"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("increase_quantity/<int:product_id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease_quantity/<int:product_id>/", views.decrease_quantity, name="decrease_quantity"),
    path('remove_from_cart/<int:product_id>/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart')
]
