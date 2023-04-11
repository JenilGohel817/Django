from django.contrib import admin
from .models import ContectModel


@admin.register(ContectModel)
class ContectAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'picture', 'gender']
