from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور', 'class': 'form-control'}
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'تکرار رمز عبور', 'class': 'form-control'}
    ))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره همراه'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'

    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        password = clean_data.get('password')
        confirmed_password = clean_data.get('confirm_password')
        if password != confirmed_password:
            raise forms.ValidationError('Password does not match!')
