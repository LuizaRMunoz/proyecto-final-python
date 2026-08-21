from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activo, Incidente

# Create your views here.
@login_required # Proteger el inicio
def home(request):
    total_activos = Activo.objects.count()
    total_incidentes = Incidente.objects.count()
    incidentes_abiertos = Incidente.objects.filter(estado='Abierto').count()

    context = {
        'total_activos': total_activos,
        'total_incidentes': total_incidentes,
        'incidentes_abiertos': incidentes_abiertos,
    }
    return render(request, 'gestion/home.html', context)

@login_required # Proteger la vista de activos
def lista_activos(request):
    activos = Activo.objects.all()
    return render(request, 'gestion/activos_list.html', {'activos': activos})

@login_required # Proteger la vista de incidentes
def lista_incidentes(request):
    incidentes = Incidente.objects.all()
    return render(request, 'gestion/incidentes_list.html', {'incidentes': incidentes})

