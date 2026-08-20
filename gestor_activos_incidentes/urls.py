"""
URL configuration for gestor_activos_incidentes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from gestion import views as gestion_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestion_views.home, name='home'),  # Página de inicio
    path('activos/', gestion_views.lista_activos, name='lista_activos'), 
    path('incidentes/', gestion_views.lista_incidentes, name='lista_incidentes'),
    path('usuarios/', include('usuarios.urls')), #Se conectan las apps de usuarios
]

# Esto permite que Django sirva las imágenes multimedia durante el desarrollo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)