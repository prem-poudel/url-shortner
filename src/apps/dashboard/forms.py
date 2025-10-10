from django import forms
from .models import ShortLink

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL',
                'required': True
            })
        }
        labels = {
            'original_url': ''
        }

class ShortLinkUpdateForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ['is_active']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }