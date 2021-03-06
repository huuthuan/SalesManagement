from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(null=True,max_length=11)
    email = models.EmailField(null=True, max_length=75)
    address = models.CharField(null=True, max_length=255)
    website = models.URLField(max_length=200, null=True, blank=True)
    description = models.CharField(null=True, max_length=255)
