# Generated by Django 4.1.1 on 2022-10-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipolaboratorio',
            name='estado',
            field=models.BooleanField(choices=[('True', 'Activo'), ('False', 'Inactivo')], default='True', verbose_name='Estado'),
        ),
    ]