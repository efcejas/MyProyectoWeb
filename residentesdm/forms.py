# Importaciones de Python estándar
import re

# Importaciones de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

# Importaciones locales
from .models import MyUsuario, Residente

# Acá van los formularios de mis usuarios

class MyUsuarioForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    es_residente = forms.BooleanField(required=False, initial=False)  # Campo para el checkbox
    es_cuerpo_admin = forms.BooleanField(required=False, initial=False)  # Campo para el checkbox
    
    # Campos adicionales comunes para residentes, médicos de staff y administrativos

    dni = forms.CharField(label='DNI', required=False, max_length=10)

    # Campos adicionales para residentes
    
    matricula = forms.CharField(label='Matrícula', required=False)
    fecha_ingreso_residencia = forms.DateField(label='Fecha de ingreso a la residencia', required=False)
    pais_nacionalidad = forms.CharField(label='País de nacionalidad', required=False)

    def clean(self):
        # Llama al método clean de la superclase (Form o ModelForm), que limpia y valida los datos del formulario
        cleaned_data = super().clean()
        
        # Obtiene los valores limpios de los campos 'first_name', 'last_name' y 'pais_nacionalidad'
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        pais_nacionalidad = cleaned_data.get('pais_nacionalidad')

        # Si 'first_name' existe y no es None, convierte 'first_name' a formato de título y actualiza 'cleaned_data'
        if first_name:
            cleaned_data['first_name'] = first_name.title()
        
        # Si 'last_name' existe y no es None, convierte 'last_name' a formato de título y actualiza 'cleaned_data'
        if last_name:
            cleaned_data['last_name'] = last_name.title()

        # Si 'pais_nacionalidad' existe y no es None, convierte 'pais_nacionalidad' a formato de título y actualiza 'cleaned_data'
        if pais_nacionalidad:
            cleaned_data['pais_nacionalidad'] = pais_nacionalidad.title()

        # Devuelve el diccionario 'cleaned_data' actualizado
        return cleaned_data

    class Meta:
        model = MyUsuario
        fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'password1', 'password2', 'es_residente', 'es_cuerpo_admin', 'dni', 'matricula', 'fecha_ingreso_residencia', 'pais_nacionalidad']
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUsuario
        fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email']
        labels = {
            'fecha_nacimiento': 'Fecha de nacimiento',
        }

class ResidenteUpdateForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['dni', 'matricula', 'fecha_ingreso_residencia', 'pais_nacionalidad']
        labels = {
            'dni': 'DNI',
            'matricula': 'Matrícula',
            'fecha_ingreso_residencia': 'Fecha de ingreso a la residencia',
            'pais_nacionalidad': 'País de nacionalidad',
        }

# Acá van los formularios de autenticación

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'}))
        
# Acá van los formularios de las sedes y demás

# Acá van los formularios de los preinformes
