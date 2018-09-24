from django.db import models

# Create your models here.
class Feature(models.Model):
    name        = models.CharField(max_length=234)
    charge_id   = models.CharField(max_length=234)