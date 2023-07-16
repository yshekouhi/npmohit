from django.contrib import admin
from .models import CustomProduct, ContactUs, AboutUs

# Register your models here.

class CustomProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    readonly_fields = ['user',]
    list_display_links = ['user', 'title']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name','title']
    list_display_links = ['full_name','title']

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'display']
    list_display_links = ['title']

admin.site.register(CustomProduct, CustomProductAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
