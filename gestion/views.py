from django.http import request
from django.shortcuts import render
from .models import Activo, Incidente

# Create your views here.
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

def lista_activos(request):
    activos = Activo.objects.all()
    return render(request, 'gestion/activos_list.html', {'activos': activos})

def lista_incidentes(request):
    incidentes = Incidente.objects.all()
    return render(request, 'gestion/incidentes_list.html', {'incidentes': incidentes})