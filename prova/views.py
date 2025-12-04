import a4
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages


def cadastrar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar.html', {'form': form})


def painel(request):
    if "usuario_id" not in request.session:
        return redirect("login")

    usuarios = Usuario.objects.filter(status=True)
    return render(request, "painel.html", {"usuarios": usuarios})


def editar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("painel")

    return render(request, "editar.html", {"form": form})


from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        senha = request.POST.get("senha", "").strip()

        print("DEBUG: tentanto login para email:", repr(email))   # debug rápido
        try:
            usuario = Usuario.objects.get(email=email)
            print("DEBUG: encontrado usuario id:", usuario.id)

            if check_password(senha, usuario.senha):
                request.session["usuario_id"] = usuario.id
                request.session["usuario_nome"] = usuario.nome
                print("DEBUG: senha ok -> redirecionando para painel")
                return redirect("painel")
            else:
                print("DEBUG: senha incorreta")
                messages.error(request, "Senha incorreta")
                return redirect("login")

        except Usuario.DoesNotExist:
            print("DEBUG: usuario nao encontrado")
            messages.error(request, "Usuário não encontrado")
            return redirect("login")

    return render(request, "login.html")


def visualizar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, "visualizar.html", {"usuario": usuario})


def excluir(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.status = False
    usuario.save()
    return redirect("painel")
