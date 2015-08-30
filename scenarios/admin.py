from scenarios.models import Scenario, ScenarioChoice, Outcome
from django.contrib import admin

class ScenarioChoiceInline(admin.StackedInline):
    model = ScenarioChoice
    extra = 4

class OutcomeInline(admin.StackedInline):
    model = Outcome

class ScenarioAdmin(admin.ModelAdmin):
    inlines = [
        ScenarioChoiceInline,
    ]

class ScenarioChoiceAdmin(admin.ModelAdmin):
    inlines = [
        OutcomeInline,
    ]

admin.site.register(Scenario, ScenarioAdmin)
