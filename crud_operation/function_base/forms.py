from django.core import validators
from django import forms
from .models import FunctionUser


class FunctionStd(forms.ModelForm):
    class Meta:
        model = FunctionUser
        fields = ['name', 'email', 'password', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'})
        }
