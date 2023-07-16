from django.forms import ModelForm
from django import forms
from .models import CustomProduct, ContactUs



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result    

class CustomProductForm(ModelForm):
    files = MultipleFileField()
    class Meta:
        model = CustomProduct
        fields = [
            'title',
            'description',
        ]
    def __init__(self, *args, **kwargs):
        super(CustomProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'عنوان'
        self.fields['description'].widget.attrs['placeholder'] = 'توضیحات'
        self.fields['files'].widget.attrs['placeholder'] = 'فایل'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-3' 


class ContactUsForm(ModelForm):
    TITLE_CHOICES  = (
    ('SELECT SUBJECT', 'موضوع پیام...'),
    ('RECOMMENT', 'پیشنهاد'),
    ('CRITIC', 'انتقاد'),
    ('FOLLOW', 'پیگیری سفارشات'),
    ('OTHER', 'سایر موضوعات')) 
    title = forms.CharField(widget=forms.Select(choices=TITLE_CHOICES), max_length= 50, required=True)
    description = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = ContactUs
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'نام و نام خانوادگی'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره تماس'
        self.fields['description'].widget.attrs['placeholder'] = 'متن پیام'



        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-3' 
        
        self.fields['title'].widget.attrs['class'] = 'form-select my-3'