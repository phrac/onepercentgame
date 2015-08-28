from django.db import models


class Scenario(models.Model):
    question = models.TextField()
    karma_value = models.NumberField()
    outcomes = models.ManyToManyField(Outcome)


class Outcome(models.Model):
    
