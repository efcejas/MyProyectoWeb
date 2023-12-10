from django import forms
from .models import Sede, Residente
import re
from django.core.exceptions import ValidationError

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['nombre', 'direccion', 'telefono', 'referente']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'referente': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Sede.objects.filter(nombre__iexact=nombre).exists():
            raise ValidationError('Ya existe una sede con ese nombre.')
        return nombre

    def save(self, commit=True):
        sede = super().save(commit=False)
        sede.nombre = sede.nombre.title()  # convierte la primera letra de cada palabra a mayúscula
        if not sede.nombre.startswith('Sede'):
            sede.nombre = 'Sede ' + sede.nombre
        sede.direccion = sede.direccion.title().replace('Avenida', 'Av.')  # convierte la primera letra de cada palabra a mayúscula y abrevia "Avenida" a "Av."
        sede.referente = sede.referente.title()  # convierte la primera letra de cada palabra a mayúscula
        sede.telefono = re.sub(r"(\d{3})(\d{4})(\d{4})", r"\1-\2-\3", sede.telefono)  # formatea el teléfono como 011-xxxx-xxxx
        if commit:
            sede.save()
        return sede

class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['nombre', 'apellido', 'DNI', 'matricula', 'email', 'nacionalidad', 'fecha_ingreso']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_DNI(self):
        DNI = self.cleaned_data.get('DNI')
        if Residente.objects.filter(DNI__iexact=DNI).exists():
            raise ValidationError('Ya existe un residente con ese DNI.')
        return DNI
        

