from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "core/index.html")

def publicacion(request):
    return render(request, "core/publicacion.html")


def registro(request):
    return render(request, "core/registro.html")

def principal(request):
    return render(request, "core/principal.html")


def buscarCuenta(request):
    return render(request, "core/buscarCuenta.html")

def info(request):
    return render(request, "core/info.html")

def perfil(request):
    return render(request, "core/perfil.html")

def editar(request):
    return render(request, "core/editar.html")

def publicar(request):
    return render(request, "core/publicar.html") 

def restablecer(request):
    return render(request, "core/restablecer.html")      

def editarCuenta(request):
    return render(request, "core/editarCuenta.html") 