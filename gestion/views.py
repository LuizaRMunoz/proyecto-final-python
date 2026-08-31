from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Activo, HistorialIncidente, Incidente, HistorialActivo
from django.contrib import messages
from .forms import ActivoForm, IncidenteForm
from django.shortcuts import get_object_or_404

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
            messages.error(request, 'Por favor, revisá el formulario. Todos los campos son obligatorios.')
    else:
        form = ActivoForm()

    activos = Activo.objects.all()
    return render(request, 'gestion/activos_list.html', {'activos': activos, 'form': form})

@login_required
def editar_activo(request, id):
    activo = get_object_or_404(Activo, id=id)
    
    if request.method == 'POST':
        password = request.POST.get('password_admin')
        
        if password != 'admin123':
            messages.error(request, 'Contraseña de administrador incorrecta. Edición cancelada.')
            return redirect('lista_activos')
            
        # Si la contraseña es correcta, seguimos con la lógica de edición
        form = ActivoForm(request.POST, instance=activo)
        motivo = request.POST.get('motivo_edicion')
        
        if form.is_valid():
            if not motivo:
                messages.error(request, 'Debes ingresar un motivo obligatorio para editar el activo.')
                return redirect('lista_activos')
                
            if form.changed_data:
                campos_modificados = ", ".join([campo.capitalize() for campo in form.changed_data])
                form.save()
                
                HistorialActivo.objects.create(
                    activo=activo,
                    usuario=request.user,
                    descripcion=f"Motivo: {motivo} | Se editaron los campos: {campos_modificados}"
                )
                
                messages.success(request, '¡Activo editado y registrado en el historial correctamente!')
            else:
                messages.info(request, 'No se detectaron cambios para guardar.')
        else:
            messages.error(request, 'Hubo un error al editar. Revisá los datos.')
            
    return redirect('lista_activos')

@login_required # Proteger la vista de incidentes
def lista_incidentes(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Incidente reportado con éxito!')
            return redirect('lista_incidentes')
        else:
            # Atrapamos el error y le avisamos al usuario
            messages.error(request, 'Por favor, revisá el formulario. Asegurate de completar todos los campos obligatorios.')
    else:
        form = IncidenteForm()

    incidentes = Incidente.objects.all()
    return render(request, 'gestion/incidentes_list.html', {'incidentes': incidentes, 'form': form})

@login_required
def editar_incidente(request, id):
    incidente = get_object_or_404(Incidente, id=id)
    
    if request.method == 'POST':
        password = request.POST.get('password_admin')
        if password != 'admin123':
            messages.error(request, 'Contraseña incorrecta. Actualización del incidente cancelada.')
            # Nota: asumo que tu ruta de la lista es 'lista_incidentes', cambialo si se llama distinto
            return redirect('lista_incidentes') 
            
        # Capturamos los datos y el comentario
        form = IncidenteForm(request.POST, instance=incidente)
        comentario_evolucion = request.POST.get('motivo_edicion')
        
        if form.is_valid():
            if not comentario_evolucion:
                messages.error(request, 'Es obligatorio relatar qué se está haciendo (comentario) para actualizar el caso.')
                return redirect('lista_incidentes')
                
            if form.changed_data:
                # Detectamos qué estado o severidad cambió para agregarlo al registro
                campos_modificados = ", ".join([campo.capitalize() for campo in form.changed_data])
                form.save()
            
                # Guardamos la evolución en la línea de tiempo
                HistorialIncidente.objects.create(
                    incidente=incidente,
                    usuario=request.user,
                    comentario=f"Evolución: {comentario_evolucion} | (Cambios técnicos: {campos_modificados})"
                )
                
                messages.success(request, '¡El incidente ha sido actualizado y registrado correctamente!')
            else:
                messages.info(request, 'No modificaste ningún dato del incidente.')
        else:
            messages.error(request, 'Hubo un error al actualizar. Revisá los campos ingresados.')
            
    return redirect('lista_incidentes')


