from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url", "slug"]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter name of website',
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'Add https:// to link',
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Use hyphen or leave blank',
            })
        }
