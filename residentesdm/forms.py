# Importaciones de Python estándar
import re

# Importaciones de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError

# Importaciones locales
from .models import MyUsuario

# Acá van los formularios de mis usuarios

class MyUsuarioForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUsuario
        fields = ['username', 'first_name', 'last_name' ,'password1', 'password2', 'email', 'fecha_nacimiento']

# Acá van los formularios de autenticación

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'}))
        
# Acá van los formularios de las sedes y demás

# Acá van los formularios de los preinformes
