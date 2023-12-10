from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Sede, Residente
from .forms import SedeForm, ResidenteForm
from django.db.models.functions import ExtractYear



# Create your views here.

# views.py
def inicio(request):
    sedes = Sede.objects.all()
    todos_los_residentes = Residente.objects.all().order_by('grupo')
    total_residentes = Residente.objects.count()
    return render(request, 'inicio.html', {'sedes': sedes, 'todos_los_residentes': todos_los_residentes, 'total_residentes': total_residentes})

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
        form = ResidenteForm(request.POST)  # Aquí estaba el error
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Residente guardado con éxito.')
            except IntegrityError:
                messages.error(request, 'Ya existe un residente con ese DNI.')
            return redirect(reverse('residentesdm:inicio'))
    else:
        form = ResidenteForm()  # Y aquí también
    return render(request, 'agregar_residente.html', {'form': form})


