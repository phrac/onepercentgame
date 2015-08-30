# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='items.Item')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='inventory_items',
            field=models.ManyToManyField(to='items.Item', null=True, through='players.PlayerInventoryItem', blank=True),
        ),
    ]
