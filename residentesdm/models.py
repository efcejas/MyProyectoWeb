# Importaciones de Django
from django.contrib.auth.models import User, AbstractUser
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

# Acá van los modelos de las actividades de los residentes

# Acá modelos relacionados con lo administrativo

