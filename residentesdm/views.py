# Importaciones de Django
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
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
from .forms import CustomPasswordChangeForm, MyUsuarioForm, UserUpdateForm, ResidenteUpdateForm
from .models import MyUsuario, Residente, CuerpoAdmin

# Vistas de los usuarios

def register(request):
    if request.method == 'POST':
        form = MyUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Verifica si se marcó como residente
            if form.cleaned_data.get('es_residente'):
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

            # Verifica si se marcó como cuerpo administrativo

            if form.cleaned_data.get('es_cuerpo_admin'):
                dni = form.cleaned_data.get('dni')

                CuerpoAdmin.objects.create(
                    usuario=user,
                    dni=dni
                )

            messages.success(request, f'Usuario {user.get_full_name()} registrado correctamente')
            return redirect('residentesdm:login')
        else:
            messages.error(request, 'Error en el registro')
    else:
        form = MyUsuarioForm()

    residente_fields = ['dni', 'matricula', 'fecha_ingreso_residencia', 'pais_nacionalidad']
    cuerpo_admin_fields = ['dni']

    return render(request, 'registration/register.html', {'form': form, 'residente_fields': residente_fields, 'cuerpo_admin_fields': cuerpo_admin_fields})

class UserProfileView(LoginRequiredMixin, DetailView):
    model = MyUsuario
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = MyUsuario
    form_class = UserUpdateForm
    second_form_class = ResidenteUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('residentesdm:perfil')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.request.user, 'residente'):
            context['form2'] = self.second_form_class(instance=self.request.user.residente)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form2 = context.get('form2')
        if form2 and form2.is_valid():
            form2.save()
        return super().form_valid(form)

# Acá las vistas relaciondas con el cambio de contraseña

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/cambiar_contraseña_form.html'
    success_url = '/password_change/done/'

# Acá vinta de la página de inicio

def inicio(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'inicio.html', {'user': user})