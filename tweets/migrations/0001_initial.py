# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_corner', models.CharField(max_length=140)),
                ('blue_corner', models.CharField(max_length=140)),
                ('end_time', models.DateTimeField(verbose_name='end time')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Battle')),
            ],
        ),
        migrations.CreateModel(
            name='TweetSpellingMistake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=140)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet')),
            ],
        ),
    ]
