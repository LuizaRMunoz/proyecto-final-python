from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save() # Guarda el nuevo usuario en la base de datos

            # Creamos el Perfil asociado automáticamente
            Perfil.objects.create(user=user)
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('login')  # Redirige al login después del registro

    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})


# Create your views here.
