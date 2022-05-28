from django.db import models

# Create your models here.
class Bottles(models.Model):
    name = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=10, decimal_places=10)
    production_date = models.DateField()
