# Generated by Django 4.2.7 on 2024-01-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentesdm', '0003_myusuario_es_residente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residente',
            name='dni',
            field=models.CharField(max_length=10, verbose_name='DNI'),
        ),
    ]