# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0007_auto_20171202_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='initial',
            field=models.CharField(max_length=2, verbose_name='initial consonant in Middle Chinese'),
        ),
    ]
