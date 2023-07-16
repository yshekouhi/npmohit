from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

class UserAccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_editable = ['is_active',]
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['date_joined',]
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','state', 'city', 'address')
    list_display_links = ('user','state', 'city', 'address')

# Register your models here.
admin.site.register(User, UserAccountAdmin)
admin.site.unregister(Group)

