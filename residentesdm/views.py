# Importaciones de Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.db import IntegrityError
from django.db.models.functions import ExtractYear
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Importaciones de la aplicación
from .forms import CustomPasswordChangeForm
from .models import MyUsuario

# acá van las vistas de mis usuarios

def register(request):
    pass

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/cambiar_contraseña_form.html'
    success_url = '/password_change/done/'
            
# Create your views here.

""" @login_required """
def inicio(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'inicio.html', {'user': user})
