from re import T
from unicodedata import name
from django.db import models


gender = (
    ('', '-----'),
    ('female', 'Female'),
    ('male', 'Male')
)


class ContectModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    picture = models.ImageField()
    gender = models.CharField(blank=True, null=True,
                              max_length=100, choices=gender)

    def __str__(self):
        return str(self.name)
