# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0002_auto_20150829_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='scenariochoice',
            name='outcomes',
        ),
        migrations.AddField(
            model_name='scenariochoice',
            name='scenario',
            field=models.ForeignKey(default='0', to='scenarios.Scenario'),
            preserve_default=False,
        ),
    ]
