# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='mc_d',
            field=models.IntegerField(verbose_name='division in Middle Chinese'),
        ),
    ]
