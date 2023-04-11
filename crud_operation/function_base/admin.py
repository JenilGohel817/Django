from django.contrib import admin
from .models import FunctionUser


# Register your models here.

@admin.register(FunctionUser)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
