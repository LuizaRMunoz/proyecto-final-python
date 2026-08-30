from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Activo, Incidente
from django.contrib import messages
from .forms import ActivoForm, IncidenteForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        total_activos = Activo.objects.count()
        total_incidentes = Incidente.objects.count()
        incidentes_abiertos = Incidente.objects.filter(estado='Abierto').count()
        incidentes_en_investigacion = Incidente.objects.filter(estado='En Investigación').count() 
        incidentes_resueltos = Incidente.objects.filter(estado='Resuelto').count()
        incidentes_cerrados = Incidente.objects.filter(estado='Cerrado').count()

        context = {
            'total_activos': total_activos,
            'total_incidentes': total_incidentes,
            'incidentes_abiertos': incidentes_abiertos,
            'incidentes_en_investigacion': incidentes_en_investigacion,
            'incidentes_resueltos': incidentes_resueltos,
            'incidentes_cerrados': incidentes_cerrados,
        }
        return render(request, 'gestion/home.html', context)
    else:
        return render(request, 'gestion/landing.html')

@login_required # Proteger la vista de activos
def lista_activos(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Activo registrado correctamente!')
            return redirect('lista_activos')
    else:
        form = ActivoForm()

    activos = Activo.objects.all()
    return render(request, 'gestion/activos_list.html', {'activos': activos, 'form': form})

@login_required # Proteger la vista de incidentes
def lista_incidentes(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Incidente reportado con éxito!')
            return redirect('lista_incidentes')
    else:
        form = IncidenteForm()

    incidentes = Incidente.objects.all()
    return render(request, 'gestion/incidentes_list.html', {'incidentes': incidentes, 'form': form})


