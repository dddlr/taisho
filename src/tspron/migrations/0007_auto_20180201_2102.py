# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0006_auto_20180201_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='note',
            field=models.CharField(blank=True, max_length=100, verbose_name='Note'),
        ),
    ]
