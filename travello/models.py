from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100, default=None)
    img = models.ImageField(upload_to='pics', default=None)
    desc = models.TextField(default=None)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
