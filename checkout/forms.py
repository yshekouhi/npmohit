from django.forms import ModelForm
from django import forms
from .models import Payment

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    zip_code = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField()
    shipping_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی'
        self.fields['state'].widget.attrs['placeholder'] = 'استان'
        self.fields['city'].widget.attrs['placeholder'] = 'شهر'
        self.fields['zip_code'].widget.attrs['placeholder'] = 'کد پستی'
        self.fields['shipping_address'].widget.attrs['placeholder'] = 'آدرس '
        self.fields['shipping_address'].widget.attrs['row'] = 3
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره همراه'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'

# class PaymentForm(forms.Form):
#     payment_method = forms.CharField(max_length=100)
#     cart_id = forms.CharField(max_length=100)
#     payment_id = forms.CharField(max_length=50)
#     amount_paid = forms.CharField(max_length=50)

#     def __init__(self, *args, **kwargs):
#         super(PaymentForm, self).__init__(*args, **kwargs)
#         self.fields['payment_method'].widget.attrs['placeholder'] = 'روش پرداخت'
#         self.fields['cart_id'].widget.attrs['placeholder'] = 'شماره کارت'
#         self.fields['payment_id'].widget.attrs['placeholder'] = 'شماره پیگیری'
#         self.fields['amount_paid'].widget.attrs['placeholder'] = 'مبلغ پرداخت'
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control my-2'            

class PaymentForm(ModelForm):
    class Meta:  
        # To specify the model to be used to create form  
        model = Payment  
        # It includes all the fields of model  
        fields = '__all__'      
