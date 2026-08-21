from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activos/', views.lista_activos, name='lista_activos'),
    path('incidentes/', views.lista_incidentes, name='lista_incidentes'),
]