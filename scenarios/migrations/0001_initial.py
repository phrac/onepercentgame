# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('karma_value', models.DecimalField(max_digits=6, decimal_places=2)),
                ('wrath_value', models.IntegerField(default=0, null=True)),
                ('greed_value', models.IntegerField(default=0, null=True)),
                ('sloth_value', models.IntegerField(default=0, null=True)),
                ('pride_value', models.IntegerField(default=0, null=True)),
                ('lust_value', models.IntegerField(default=0, null=True)),
                ('envy_value', models.IntegerField(default=0, null=True)),
                ('gluttony_value', models.IntegerField(default=0, null=True)),
                ('outcome_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('level', models.IntegerField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scenario', models.ForeignKey(to='scenarios.Scenario')),
            ],
        ),
        migrations.AddField(
            model_name='outcome',
            name='scenario',
            field=models.ForeignKey(to='scenarios.ScenarioChoice'),
        ),
    ]
