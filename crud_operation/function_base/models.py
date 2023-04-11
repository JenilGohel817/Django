from django.db import models


# Create your models here.
gender = (
    ('', '-----'),
    ('female', 'Female'),
    ('male', 'Male')
)


class FunctionUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(blank=True, null=True, max_length=100, choices=gender)
