from django.db import models

# Create your models here.

class Sede(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    referente = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
