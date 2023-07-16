from django.contrib import admin
from .models import Item, CategoryService


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = { 'slug': ['title'],}

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'display']
    prepopulated_fields = { 'slug': ['title'],}
    list_editable = ['order', 'display']
    ordering = ['order',]

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
