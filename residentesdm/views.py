from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Sede
from .forms import SedeForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def evaluacion(request):
    return render(request, 'evaluacion.html')

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


