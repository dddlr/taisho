# Generated by Django 2.2.1 on 2019-06-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0030_auto_20190611_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pron_note',
            field=models.TextField(blank=True, verbose_name='Pronunciation note'),
        ),
    ]
