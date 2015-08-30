# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0004_auto_20150830_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenariochoice',
            name='inventory_required',
            field=models.ManyToManyField(default=None, to='items.Item', blank=True),
        ),
    ]
