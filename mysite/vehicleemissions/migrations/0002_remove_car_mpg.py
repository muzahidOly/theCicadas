# Generated by Django 4.1.1 on 2023-01-28 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleemissions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='mpg',
        ),
    ]
