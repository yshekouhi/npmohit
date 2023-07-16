from django.urls import path
from .views import CustomProductCreateView

app_name = 'pages'

urlpatterns = [
    path("custom_product/", CustomProductCreateView.as_view(), name="custom_product"),
]