# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-17 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0021_auto_20180717_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='own_note',
            field=models.CharField(blank=True, max_length=50, verbose_name='my own note'),
        ),
    ]
