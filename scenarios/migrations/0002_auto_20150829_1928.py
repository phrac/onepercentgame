# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outcome',
            name='scenario',
        ),
        migrations.RemoveField(
            model_name='scenariochoice',
            name='scenario',
        ),
        migrations.AddField(
            model_name='scenario',
            name='choices',
            field=models.ManyToManyField(to='scenarios.ScenarioChoice'),
        ),
        migrations.AddField(
            model_name='scenariochoice',
            name='choice_text',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenariochoice',
            name='outcomes',
            field=models.ManyToManyField(to='scenarios.Outcome'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='level',
            field=models.IntegerField(null=True),
        ),
    ]
