from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, UserUpdateForm, PerfilUpdateForm
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

@login_required
def perfil(request):
    # Intentamos obtener o crear el perfil si no existiera
    perfil_usuario, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil_usuario)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Tu perfil ha sido actualizado correctamente!")
            return redirect('perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil_usuario)

    return render(request, 'usuarios/perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Esto borra al User y a su Perfil (gracias al cascade)
        messages.success(request, 'Tu cuenta ha sido eliminada correctamente.')
        return redirect('login')  # Lo mandamos a la pantalla de login
    
    # Si alguien intenta entrar por la URL directo, lo devolvemos al perfil
    return redirect('perfil')