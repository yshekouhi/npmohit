from django.contrib import admin
from .models import Product, Specifications, Category


class SpecificationsInline(admin.TabularInline):
    extra = 0
    model = Specifications
    classes = ['collapse']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'available', 'price', 'unit', 'featured', 'recent_product')
    list_display_links = ('title', 'category')
    prepopulated_fields = { 'slug': ['title'],}
    inlines = [SpecificationsInline,]
    list_filter =  ['available',]
    list_select_related = ["category",]
    radio_fields = {"category": admin.HORIZONTAL}



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Category 



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

