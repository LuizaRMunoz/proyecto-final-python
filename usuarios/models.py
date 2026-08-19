from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    ROLES = [
        ('Analista', 'Analista de Seguridad'),
        ('Administrador', 'Administrador de IT'),
        ('Auditor', 'Auditor Interno'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    role = models.CharField(max_length=20, choices=ROLES, default='Analista')
    departamento = models.CharField(max_length=100, blank=True, verbose_name="Departamento o Área")
    bio = models.TextField(blank=True, verbose_name="Biografía o Notas")
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)

def __str__(self):
        return f"Perfil de {self.user.username} ({self.rol})"