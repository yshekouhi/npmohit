from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('password_validate/<uidb64>/<token>', views.password_validate, name='password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
