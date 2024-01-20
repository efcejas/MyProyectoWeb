# Importaciones de Python estándar
import re

# Importaciones de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

# Importaciones locales
from .models import MyUsuario

# Acá van los formularios de mis usuarios

class MyUsuarioForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    es_residente = forms.BooleanField(required=False, initial=False)  # Campo para el checkbox

    # Campos adicionales para residentes
    dni = forms.CharField(required=False, max_length=10)
    matricula = forms.CharField(required=False)
    fecha_ingreso_residencia = forms.DateField(required=False)
    pais_nacionalidad = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name:
            cleaned_data['first_name'] = first_name.title()
        if last_name:
            cleaned_data['last_name'] = last_name.title()

        return cleaned_data

    class Meta:
        model = MyUsuario
        fields = ['username', 'first_name', 'last_name', 'fecha_nacimiento', 'email', 'password1', 'password2', 'es_residente']

# Acá van los formularios de autenticación

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'}))
        
# Acá van los formularios de las sedes y demás

# Acá van los formularios de los preinformes
