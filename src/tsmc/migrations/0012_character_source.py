# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0011_auto_20180105_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='source',
            field=models.CharField(blank=True, max_length=1, verbose_name='source (b = dad, m = mum, u = me but unverified)'),
        ),
    ]