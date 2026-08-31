from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, verbose_name="Biografía o Notas")
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"