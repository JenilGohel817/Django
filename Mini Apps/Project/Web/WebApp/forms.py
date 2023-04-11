from dataclasses import field
from tkinter import Widget
from django import forms
from .models import ContactModal


class ContectForm(forms.ModelForm):
    class Meta:
        model = ContactModal
        fields = '__all__'
        Widgets = {
            'name': forms.TextInput(),
            'gender': forms.Select(),
        }
