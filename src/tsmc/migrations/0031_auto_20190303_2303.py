# Generated by Django 2.1.1 on 2019-03-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0030_auto_20190303_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial',
            name='other',
            field=models.CharField(blank=True, max_length=4, verbose_name='Other initials this encompasses'),
        ),
    ]
