# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
