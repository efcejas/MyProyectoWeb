from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Acá van los modelos de mis usuarios

class MedicoResidente(User):
    DNI = models.CharField(max_length=10, unique=True, primary_key=True)
    fecha_nacimiento = models.DateField()
    matricula = models.CharField(max_length=6, unique=True)
    nacionalidad = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()

    def save(self, *args, **kwargs):
        # Formatear el DNI antes de guardarlo
        self.DNI = '{}.{}.{}'.format(self.DNI[:2], self.DNI[2:5], self.DNI[5:])
        
        # Formatear el nombre y apellido
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

        super().save(*args, **kwargs)

class MedicoStaff(User):
    DNI = models.CharField(max_length=10, unique=True, primary_key=True)
    fecha_nacimiento = models.DateField()
    matricula = models.CharField(max_length=6, unique=True)
    

    def save(self, *args, **kwargs):
        # Formatear el DNI antes de guardarlo
        self.DNI = '{}.{}.{}'.format(self.DNI[:2], self.DNI[2:5], self.DNI[5:])
        
        # Formatear el nombre y apellido
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

        super().save(*args, **kwargs)

class CuerpoAdmin(User):
    DNI = models.CharField(max_length=10, unique=True, primary_key=True)
    fecha_nacimiento = models.DateField()

    def save(self, *args, **kwargs):
        # Formatear el DNI antes de guardarlo
        self.DNI = '{}.{}.{}'.format(self.DNI[:2], self.DNI[2:5], self.DNI[5:])
        
        # Formatear el nombre y apellido
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

        super().save(*args, **kwargs)

# Acá van los modelos de las actividades de los residentes

class Preinforme(models.Model):
    residente = models.ForeignKey(MedicoResidente, on_delete=models.CASCADE, related_name='preinformes')
    contenido = models.TextField()
    nombre_paciente = models.CharField(max_length=200)
    apellido_paciente = models.CharField(max_length=200)
    dni_paciente = models.CharField(max_length=10)
    fecha_estudio = models.DateField()

    def save(self, *args, **kwargs):
        # Formatear el DNI del paciente antes de guardarlo
        self.dni_paciente = '{}.{}.{}'.format(self.dni_paciente[:2], self.dni_paciente[2:5], self.dni_paciente[5:])

        # Formatear el nombre y apellido del paciente
        self.nombre_paciente = self.nombre_paciente.title()
        self.apellido_paciente = self.apellido_paciente.title()

        super().save(*args, **kwargs)

# Create your models here.

class Preinforme(models.Model):
    residente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preinformes')
    contenido = models.TextField()
    # otros campos necesarios...

""" Tengo que crear la base de datos para los residentes, docentes y donde se guardarán los preinformes con las correcciones. 

class Preinforme(models.Model):
    residente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preinformes')
    contenido = models.TextField()
    # otros campos necesarios...

class Correccion(models.Model):
    preinforme = models.ForeignKey(Preinforme, on_delete=models.CASCADE, related_name='correcciones')
    docente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='correcciones')
    contenido = models.TextField()

    # otros campos necesarios..."""

# Clases accesorias

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
        return f"{self.apellido.title()}, {self.nombre.title()}"
