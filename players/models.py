from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    turns_played = models.IntegerField(default=0)
    percent_level = models.NumberField(max_digits=4, decimal_places=2)
    money = models.DecimalField(max_digits=15, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
