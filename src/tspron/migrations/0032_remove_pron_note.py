# Generated by Django 2.2.1 on 2019-06-12 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tspron', '0031_word_pron_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pron',
            name='note',
        ),
    ]
