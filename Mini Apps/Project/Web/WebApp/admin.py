from django.contrib import admin
from .models import ContactModal
# Register your models here.


@admin.register(ContactModal)
class Contectadmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'gender']
