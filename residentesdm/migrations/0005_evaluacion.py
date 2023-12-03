# Generated by Django 4.2.7 on 2023-12-03 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residentesdm', '0004_residente_email_alter_residente_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positivos', models.TextField(blank=True, null=True)),
                ('negativos', models.TextField(blank=True, null=True)),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residentesdm.residente')),
            ],
        ),
    ]