# Generated by Django 2.1.1 on 2019-03-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmc', '0029_initial_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial',
            name='other',
            field=models.CharField(blank=True, max_length=5, verbose_name='Other initials this encompasses'),
        ),
    ]
