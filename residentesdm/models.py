from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Sede(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    referente = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

class Residente(models.Model):
    dni_regex = RegexValidator(
        regex=r'^\d{2}\.\d{3}\.\d{3}$',
        message="El DNI debe tener el formato: 'xx.xxx.xxx'"
    )
    matricula_regex = RegexValidator(
        regex=r'^\d{3}\.\d{3}$',
        message="La matrícula debe tener el formato: 'xxx.xxx'"
    )

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.CharField(validators=[dni_regex], max_length=10, unique=True, primary_key=True, default='00.000.000')
    matricula = models.CharField(validators=[matricula_regex], max_length=10, unique=True, default='000.000')
    email = models.EmailField(max_length=200, default='Desconocido')
    nacionalidad = models.CharField(max_length=200, default='Desconocida')
    fecha_ingreso = models.DateField()
    repetido = models.BooleanField(default=False)
    grupo = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        self.grupo = self.calculate_grupo()
        super().save(*args, **kwargs)

    def calculate_grupo(self):
        hoy = timezone.now().date()
        diferencia = hoy.year - self.fecha_ingreso.year - ((hoy.month, hoy.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day))

        if self.repetido:
            diferencia -= 1

        if diferencia < 1:
            return 'R1'
        elif diferencia < 2:
            return 'R2'
        elif diferencia < 3:
            return 'R3'
        elif diferencia < 4:
            return 'R4'
        else:
            return 'Egresado'

    def __str__(self):
        return f"{self.apellido.title()}, {self.nombre.title()}, {self.DNI} - {self.grupo}"


