# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-31 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0017_auto_20180128_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taishanese',
            name='source',
            field=models.CharField(max_length=1, verbose_name='source (d = dad, m = mum, u = me but unverified)'),
        ),
    ]
