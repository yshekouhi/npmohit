from django import forms
from newsletter.models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'is_verified']
        widgets = {
            'is_verified': forms.HiddenInput(),  # Hide the verification field in the form
        }

