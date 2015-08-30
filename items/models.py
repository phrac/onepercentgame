from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=32)
    cash_value = models.DecimalField(max_digits=11, decimal_places=2)
    
