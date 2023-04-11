from django import forms
from .models import ClassUser


class ClassStd(forms.ModelForm):
    class Meta:
        model = ClassUser
        fields = ['name', 'email', 'password', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
