# Generated by Django 4.1.1 on 2022-10-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='costo',
        ),
    ]