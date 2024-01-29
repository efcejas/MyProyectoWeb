# Importaciones de Django
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Importaciones de Python estándar
from datetime import timedelta

# Importaciones de terceros
from ckeditor.fields import RichTextField # Para el campo de texto enriquecido

# Acá van los modelos de mis usuarios

class MyUsuario(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_residente = models.BooleanField(default=False) # Agrega el campo es_residente
    es_administrativo = models.BooleanField(default=False) # Agrega el campo es_administrativo
    
class Residente(models.Model):
    usuario = models.OneToOneField(MyUsuario, on_delete=models.CASCADE)
    dni = models.CharField('DNI', max_length=10, unique=True)
    matricula = models.CharField('Matrícula', max_length=20)
    fecha_ingreso_residencia = models.DateField('Fecha de Ingreso')
    pais_nacionalidad = models.CharField('País de Nacionalidad', max_length=50)

    def __str__(self):
        return f'{self.usuario.last_name} {self.usuario.first_name}'

class CuerpoAdmin(models.Model):
    usuario = models.OneToOneField(MyUsuario, on_delete=models.CASCADE)
    dni = models.CharField('DNI', max_length=10, unique=True)
    
    def __str__(self):
        return f'{self.usuario.last_name} {self.usuario.first_name}'

# Acá van los modelos de las actividades de los residentes

# Acá modelos relacionados con lo administrativo

