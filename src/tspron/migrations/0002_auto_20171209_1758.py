# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='char',
            field=models.CharField(max_length=10, verbose_name='Chinese word or phrase'),
        ),
    ]
