# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0003_auto_20180105_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='gloss',
            field=models.CharField(max_length=50, verbose_name='Gloss'),
        ),
    ]