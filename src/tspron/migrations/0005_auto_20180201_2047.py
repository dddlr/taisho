# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0004_auto_20180105_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='pron',
            field=models.CharField(max_length=50, verbose_name='Pronunciation'),
        ),
    ]