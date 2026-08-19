from django.contrib import admin
from .models import Activo, Incidente

# Register your models here.

@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'criticidad', 'ubicacion_ip', 'fecha_registro')
    list_filter = ('tipo', 'criticidad')
    search_fields = ('nombre', 'ubicacion_ip')

@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo_afectado', 'severidad', 'estado', 'reportado_por', 'fecha_reporte')
    list_filter = ('severidad', 'estado')
    search_fields = ('titulo', 'descripcion')