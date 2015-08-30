# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150830_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='inventory_items',
            field=models.ManyToManyField(default=None, to='items.Item', through='players.PlayerInventoryItem', blank=True),
        ),
    ]
