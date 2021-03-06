# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('turns_played', models.IntegerField(default=0)),
                ('money', models.DecimalField(default=500.0, max_digits=15, decimal_places=2)),
                ('game_age', models.IntegerField(default=18)),
                ('percent_level', models.DecimalField(max_digits=4, decimal_places=2)),
                ('karma_level', models.IntegerField(default=25)),
                ('wrath_level', models.IntegerField(default=0)),
                ('greed_level', models.IntegerField(default=0)),
                ('sloth_level', models.IntegerField(default=0)),
                ('pride_level', models.IntegerField(default=0)),
                ('lust_level', models.IntegerField(default=0)),
                ('envy_level', models.IntegerField(default=0)),
                ('gluttony_level', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
