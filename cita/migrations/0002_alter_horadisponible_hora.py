# Generated by Django 4.1.1 on 2022-11-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horadisponible',
            name='hora',
            field=models.TimeField(verbose_name='Hora Disponible'),
        ),
    ]
