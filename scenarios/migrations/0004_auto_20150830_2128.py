# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('scenarios', '0003_auto_20150829_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariochoice',
            name='cash_required',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='scenariochoice',
            name='inventory_required',
            field=models.ManyToManyField(default=None, to='items.Item', null=True, blank=True),
        ),
    ]
