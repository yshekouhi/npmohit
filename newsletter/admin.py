from django.contrib import admin
from .models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_verified')
    list_filter = ['is_verified']

admin.site.register(Subscriber, SubscriberAdmin)

