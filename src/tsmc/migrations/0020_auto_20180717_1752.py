# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-17 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0019_auto_20180717_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='variants',
            new_name='variant',
        ),
    ]