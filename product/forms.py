from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = [
            'title',
            'slug',
            'category',
            'image',
            'media',
            'description',
            'price',
            'featured',
            'recent_product',
        ]  
        def clean_field(self):
            description = self.cleaned_data["description"]
            if len(description) < 6:
                raise forms.validationError("The description is too short")              