# Generated by Django 4.2.7 on 2024-01-20 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentesdm', '0002_residente'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusuario',
            name='es_residente',
            field=models.BooleanField(default=False),
        ),
    ]
