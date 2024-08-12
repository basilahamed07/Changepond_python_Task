from django.db import models

# Create your models here.
class Dishes(models.Model):
    Dishname = models.CharField(max_length=100)
    price = models.IntegerField()
    