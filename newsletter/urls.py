from django.urls import path
from newsletter.views import subscribe, verify_email

app_name = 'newsletter'
urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('verify/<uuid:token>/', verify_email, name='verify_email'),
]
