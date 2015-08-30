from django.db import models
from items.models import Item


class Scenario(models.Model):
    question = models.TextField()
    level = models.IntegerField(null=True)
    
class ScenarioChoice(models.Model):
    scenario = models.ForeignKey(Scenario)
    choice_text = models.TextField()
    inventory_required = models.ManyToManyField(Item, default=None,
                                                blank=True)
    cash_required = models.DecimalField(max_digits=11, decimal_places=2,
                                        default=0, blank=True)

class Outcome(models.Model):
    models.ForeignKey(ScenarioChoice)
    karma_value = models.DecimalField(max_digits=6, decimal_places=2)
    wrath_value = models.IntegerField(default=0, null=True)
    greed_value = models.IntegerField(default=0, null=True)
    sloth_value = models.IntegerField(default=0, null=True)
    pride_value = models.IntegerField(default=0, null=True)
    lust_value = models.IntegerField(default=0, null=True)
    envy_value = models.IntegerField(default=0, null=True)
    gluttony_value = models.IntegerField(default=0, null=True)

    outcome_text = models.TextField()
    


    
