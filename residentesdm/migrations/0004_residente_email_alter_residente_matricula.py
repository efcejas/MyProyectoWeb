# Generated by Django 4.2.7 on 2023-12-03 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentesdm', '0003_remove_residente_dni_residente_matricula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='residente',
            name='email',
            field=models.EmailField(default='Desconocido', max_length=200),
        ),
        migrations.AlterField(
            model_name='residente',
            name='matricula',
            field=models.CharField(default='000.000', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="La matrícula debe tener el formato: 'xxx.xxx'", regex='^\\d{3}\\.\\d{3}$')]),
        ),
    ]
