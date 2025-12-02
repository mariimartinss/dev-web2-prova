import a4
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Usuario
from .forms import UsuarioForm

def cadastrar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar.html', {'form': form})


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.senha==senha:
                return render(request, 'usuario_logado.html', {'usuario': usuario})
            else:
                return render(request, 'senha_incorreta.html', {'usuario': usuario})
        except Usuario.DoesNotExist:

            return render(request, 'usuario_nao_encontrado.html', {'email': email})

    return render(request, 'login.html')