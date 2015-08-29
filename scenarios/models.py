from django.db import models


class Scenario(models.Model):
    question = models.TextField()
    level = models.IntegerField(max_length=3, null=True)
    
class ScenarioChoice(models.Model):
    scenario = models.ForeignKey(Scenario)

class Outcome(models.Model):
    scenario = models.ForeignKey(ScenarioChoice)
    karma_value = models.DecimalField(max_digits=6, decimal_places=2)
    wrath_value = models.IntegerField(default=0, null=True)
    greed_value = models.IntegerField(default=0, null=True)
    sloth_value = models.IntegerField(default=0, null=True)
    pride_value = models.IntegerField(default=0, null=True)
    lust_value = models.IntegerField(default=0, null=True)
    envy_value = models.IntegerField(default=0, null=True)
    gluttony_value = models.IntegerField(default=0, null=True)

    outcome_text = models.TextField()
    


    
