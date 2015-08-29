from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    turns_played = models.IntegerField(default=0)
    money = models.DecimalField(max_digits=15, decimal_places=2, default=500.00)
    game_age = models.IntegerField(default=18)

    percent_level = models.DecimalField(max_digits=4, decimal_places=2)
    karma_level = models.IntegerField(default=25)
    wrath_level = models.IntegerField(default=0)
    greed_level = models.IntegerField(default=0)
    sloth_level = models.IntegerField(default=0)
    pride_level = models.IntegerField(default=0)
    lust_level = models.IntegerField(default=0)
    envy_level = models.IntegerField(default=0)
    gluttony_level = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
