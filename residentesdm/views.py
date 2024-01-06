from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required # para que solo los usuarios logueados puedan acceder a las vistas
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Sede, Residente, MedicoResidente
from .forms import SedeForm, ResidenteForm, MedicoResidenteForm
from django.db.models.functions import ExtractYear

# acá van las vistas de mis usuarios

def register(request):
    if request.method == 'POST':
        form = MedicoResidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('residentesdm:login')  # redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = MedicoResidenteForm()
    return render(request, 'registration/register.html', {'form': form})

# Create your views here.

""" 

from django.utils.decorators import method_decorator
from django.views import View
from .models import Preinforme, Correccion

@method_decorator(login_required, name='dispatch')
class PreinformeView(View):
    def get(self, request):
        # obtener los preinformes del usuario actual
        preinformes = Preinforme.objects.filter(residente=request.user)
        # renderizar a una plantilla con los preinformes

    def post(self, request):
        # crear un nuevo preinforme
        preinforme = Preinforme.objects.create(residente=request.user, contenido=request.POST['contenido'])
        # redirigir a la página de detalles del preinforme

@method_decorator(login_required, name='dispatch')
class CorreccionView(View):
    def post(self, request, preinforme_id):
        # asegurarse de que el usuario actual es un docente
        if not request.user.is_staff:
            return HttpResponseForbidden()
        # crear una nueva corrección
        correccion = Correccion.objects.create(docente=request.user, preinforme_id=preinforme_id, contenido=request.POST['contenido'])
        # redirigir a la página de detalles del preinforme 
"""
@login_required
def inicio(request):
    sedes = Sede.objects.all()
    todos_los_residentes = Residente.objects.all().order_by('grupo', 'nombre')
    total_residentes = Residente.objects.count()
    return render(request, 'inicio.html', {'sedes': sedes, 'todos_los_residentes': todos_los_residentes, 'total_residentes': total_residentes, 'user': request.user})

def admin_panel(request):
    todos_los_residentes = Residente.objects.all().order_by('grupo', 'nombre')
    total_residentes = Residente.objects.count()
    return render(request, 'admin_panel.html', {'todos_los_residentes': todos_los_residentes, 'total_residentes': total_residentes})

def sedes(request):
    sedes = Sede.objects.all()
    return render(request, 'sedes.html', {'sedes': sedes})

def agregarsede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Sede guardada con éxito.')
            except IntegrityError:
                messages.error(request, 'Ya existe una sede con ese nombre.')
            return redirect(reverse('residentesdm:sedes'))
            # no funcionaba en un principio porque no había puesto 'residentesdm:' antes de 'sedes'.
    else:
        form = SedeForm()
    return render(request, 'agregarsede.html', {'form': form})

def agregar_residente(request):
    if request.method == 'POST':
        form = ResidenteForm(request.POST)
        if form.is_valid():
            try:
                residente = form.save()
                messages.success(request, f'Se agregó exitosamente al residente {residente.nombre.title()} {residente.apellido.title()}.')
            except IntegrityError:
                messages.error(request, 'Ya existe un residente con ese DNI.')
            return redirect(reverse('residentesdm:admin_panel') + '?tab=residents')
    else:
        form = ResidenteForm()
    return render(request, 'agregar_residente.html', {'form': form})

def residentes(request):
    todos_los_residentes = Residente.objects.all().order_by('grupo')
    total_residentes = Residente.objects.count()

    # Divide los residentes por año
    residentes_primer_año = [r for r in todos_los_residentes if r.calculate_grupo() == 'R1']
    residentes_segundo_año = [r for r in todos_los_residentes if r.calculate_grupo() == 'R2']
    residentes_tercer_año = [r for r in todos_los_residentes if r.calculate_grupo() == 'R3']
    residentes_cuarto_año = [r for r in todos_los_residentes if r.calculate_grupo() == 'R4']

    return render(request, 'residentes.html', {
        'todos_los_residentes': todos_los_residentes,
        'total_residentes': total_residentes,
        'residentes_primer_año': residentes_primer_año,
        'residentes_segundo_año': residentes_segundo_año,
        'residentes_tercer_año': residentes_tercer_año,
        'residentes_cuarto_año': residentes_cuarto_año,
    })

def supervision_residentes(request):
    return render(request, 'supervision_residentes.html')