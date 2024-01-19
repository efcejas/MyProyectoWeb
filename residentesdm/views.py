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
from .models import MyUsuario

# Vistas de los usuarios

def register(request):
    if request.method == 'POST':
        form = MyUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('residentesdm:login')
        else:
            messages.error(request, 'Error en el registro')
    else:
        form = MyUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/cambiar_contraseña_form.html'
    success_url = '/password_change/done/'

@login_required
def inicio(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'inicio.html', {'user': user})