# Importaciones de Django
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.db import IntegrityError
from django.db.models.functions import ExtractYear
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Importaciones de la aplicación
from .forms import CustomPasswordChangeForm, MyUsuarioForm
from .models import MyUsuario, Residente

# Vistas de los usuarios

def register(request):
    if request.method == 'POST':
        form = MyUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Verifica si se marcó como residente
            if request.POST.get('es_residente'):
                dni = form.cleaned_data.get('dni')
                matricula = form.cleaned_data.get('matricula')
                fecha_ingreso_residencia = form.cleaned_data.get('fecha_ingreso_residencia')
                pais_nacionalidad = form.cleaned_data.get('pais_nacionalidad')

                Residente.objects.create(
                    usuario=user,
                    dni=dni,
                    matricula=matricula,
                    fecha_ingreso_residencia=fecha_ingreso_residencia,
                    pais_nacionalidad=pais_nacionalidad
                )

            messages.success(request, 'Usuario registrado correctamente')
            return redirect('residentesdm:login')
        else:
            messages.error(request, 'Error en el registro')
    else:
        form = MyUsuarioForm()

    residente_fields = ['dni', 'matricula', 'fecha_ingreso_residencia', 'pais_nacionalidad']
    return render(request, 'registration/register.html', {'form': form, 'residente_fields': residente_fields})

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/cambiar_contraseña_form.html'
    success_url = '/password_change/done/'

def inicio(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'inicio.html', {'user': user})