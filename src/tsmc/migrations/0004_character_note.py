# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0003_auto_20171126_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='note',
            field=models.CharField(default='', max_length=10, verbose_name='note on character'),
        ),
    ]
