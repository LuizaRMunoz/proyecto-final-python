from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activo(models.Model):
    TIPOS_ACTIVO = [
        ('Servidor', 'Servidor / Máquina Virtual'),
        ('Base_de_Datos', 'Base de Datos'),
        ('Red', 'Dispositivo de Red (Router/Switch/Firewall)'),
        ('Equipo_Usuario', 'Equipo de Usuario / Laptop'),
        ('Aplicacion', 'Aplicación Web / API'),
    ]

    NIVELES_CRITICIDAD = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]

    nombre = models.CharField(max_length=150, verbose_name="Nombre del Activo")
    tipo = models.CharField(max_length=30, choices=TIPOS_ACTIVO, default='Servidor')
    criticidad = models.CharField(max_length=10, choices=NIVELES_CRITICIDAD, default='Media')
    ubicacion_ip = models.CharField(max_length=100, verbose_name="Dirección IP / Ubicación")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()}) - Criticidad: {self.get_criticidad_display()}"

class HistorialActivo(models.Model):
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE, related_name='historial')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Quién lo hizo
    fecha_modificacion = models.DateTimeField(auto_now_add=True) # Cuándo lo hizo
    descripcion = models.TextField() # Qué cambió y el motivo

    def __str__(self):
        return f"Modificación en {self.activo.nombre} - {self.fecha_modificacion.strftime('%d/%m/%Y')}"

class Incidente(models.Model):
    NIVELES_SEVERIDAD = [
        ('Critico', 'Crítico'),
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    ]

    ESTADOS_INCIDENTE = [
        ('Abierto', 'Abierto'),
        ('En_Investigacion', 'En Investigación'),
        ('Resuelto', 'Resuelto'),
        ('Cerrado', 'Cerrado'),
    ]


    titulo = models.CharField(max_length=200, verbose_name="Título del Incidente")
    descripcion = models.TextField(verbose_name="Descripción del Suceso")
    severidad = models.CharField(max_length=10, choices=NIVELES_SEVERIDAD, default='Medio')
    estado = models.CharField(max_length=20, choices=ESTADOS_INCIDENTE, default='Abierto')

    # Relaciones:
    activo_afectado = models.ForeignKey(Activo, on_delete=models.CASCADE, related_name='incidentes', verbose_name="Activo Afectado")
    reportado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='incidentes_reportados', verbose_name="Reportado Por")

    fecha_reporte = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_reporte']

    def __str__(self):
        return f"[{self.severidad}] {self.titulo} - Estado: {self.get_estado_display()}"

class HistorialIncidente(models.Model):
    incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE, related_name='historial')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Quién actualizó el caso
    fecha_modificacion = models.DateTimeField(auto_now_add=True) # Cuándo lo hizo
    comentario = models.TextField() # El relato de lo que se hizo y los campos que cambiaron

    def __str__(self):
        return f"Actualización en {self.incidente.titulo} - {self.fecha_modificacion.strftime('%d/%m/%Y')}"