from django.db import models
import datetime

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField(("Date"), default=datetime.date.today)
