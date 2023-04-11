from django.contrib import admin
from .models import ClassUser


# Register your models here.

@admin.register(ClassUser)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'gender')
