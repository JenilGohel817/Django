from django.db import models

# Create your models here.

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class ContactModal(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    gender = models.CharField(null=True, blank=True,
                              choices=gender, max_length=100)
