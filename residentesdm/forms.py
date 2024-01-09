from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from .models import Sede, Residente, MedicoResidente, MedicoStaff, CuerpoAdmin, Preinforme
import re
from django.core.exceptions import ValidationError

# Acá van los formularios de mis usuarios

class MedicoResidenteForm(UserCreationForm):
    class Meta:
        model = MedicoResidente
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'DNI', 'fecha_nacimiento', 'matricula', 'email', 'nacionalidad', 'fecha_ingreso']

    def __init__(self, *args, **kwargs):
        super(MedicoResidenteForm, self).__init__(*args, **kwargs)
        self.fields['matricula'].label = "Matrícula"
        self.fields['fecha_nacimiento'].label = "Fecha de nacimiento"
        self.fields['fecha_ingreso'].label = "Fecha de ingreso a la residencia"

class MedicoStaffForm(UserCreationForm):
    class Meta:
        model = MedicoStaff
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'DNI', 'matricula', 'email']

    def __init__(self, *args, **kwargs):
        super(MedicoStaffForm, self).__init__(*args, **kwargs)
        self.fields['matricula'].label = "Matrícula"

class CuerpoAdminForm(UserCreationForm):
    class Meta:
        model = CuerpoAdmin
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'DNI', 'email']

    def __init__(self, *args, **kwargs):
        super(CuerpoAdminForm, self).__init__(*args, **kwargs)


# Acá van los formularios de autenticación

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'}))
        
# Acá van los formularios de las sedes y demás

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
        # Agrega los puntos al DNI
        DNI = '{}.{}.{}'.format(DNI[:2], DNI[2:5], DNI[5:])
        return DNI

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        # Agrega los puntos a la matrícula
        matricula = '{}.{}'.format(matricula[:3], matricula[3:])
        return matricula
        
# Acá van los formularios de los preinformes

class PreinformeForm(forms.ModelForm):
    fecha_estudio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Preinforme
        fields = ['residente', 'nombre_paciente', 'apellido_paciente', 'dni_paciente', 'fecha_estudio', 'cuerpo_preinforme']
        widgets = {
            'residente': forms.TextInput(attrs={'placeholder': 'Residente', 'class': 'form-control'}),
            'nombre_paciente': forms.TextInput(attrs={'placeholder': 'Nombre del paciente', 'class': 'form-control'}),
            'apellido_paciente': forms.TextInput(attrs={'placeholder': 'Apellido del paciente', 'class': 'form-control'}),
            'dni_paciente': forms.NumberInput(attrs={'placeholder': 'DNI del paciente', 'class': 'form-control'}),
            'cuerpo_preinforme': forms.Textarea(attrs={'placeholder': 'Escriba el preinforme aquí...', 'class': 'form-control'}),
        }