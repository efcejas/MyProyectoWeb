# Generated by Django 4.2.7 on 2023-12-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentesdm', '0005_evaluacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
    ]