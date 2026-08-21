from django import forms
from .models import Activo, Incidente

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['nombre', 'tipo', 'criticidad', 'ubicacion_ip', 'descripcion']

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['titulo', 'descripcion', 'activo_afectado', 'severidad', 'estado']