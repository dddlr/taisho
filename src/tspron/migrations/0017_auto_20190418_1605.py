# Generated by Django 2.1.1 on 2019-04-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0016_word_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='note',
            field=models.TextField(verbose_name='Note'),
        ),
    ]
