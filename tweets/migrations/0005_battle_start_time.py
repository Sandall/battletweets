# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_remove_battle_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='start_time',
            field=models.DateTimeField(default=None, verbose_name='start time'),
        ),
    ]
