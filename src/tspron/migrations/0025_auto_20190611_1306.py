# Generated by Django 2.2.1 on 2019-06-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0024_auto_20190611_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='pron_old',
            field=models.CharField(blank=True, max_length=75, verbose_name='Pronunciation (old)'),
        ),
    ]
