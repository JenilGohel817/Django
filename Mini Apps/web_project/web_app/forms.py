from pyexpat import model
from tkinter import Widget
from django import forms
from .models import ContectModel


class ContectForm(forms.ModelForm):
    class Meta:
        model = ContectModel
        fields = '__all__'
        Widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
            'gender': forms.Select(),
        }
