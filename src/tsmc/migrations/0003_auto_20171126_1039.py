# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0002_auto_20171125_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='mc_d',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mc_f',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mc_i',
            new_name='initial',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mc_o',
            new_name='openness',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='mc_t',
            new_name='tone',
        ),
        migrations.RenameField(
            model_name='taishanese',
            old_name='ts_f',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='taishanese',
            old_name='ts_i',
            new_name='initial',
        ),
        migrations.RenameField(
            model_name='taishanese',
            old_name='ts_t',
            new_name='tone',
        ),
    ]
