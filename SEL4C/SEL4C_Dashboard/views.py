from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from json import loads, dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from api.models import Usuario
import requests

# Create your views here.
# endpoints
def index(request):
    return render(request, "Pagina_principal/index.html")


def descargar_app(request):
    return render(request, "Pagina_principal/descargar.html")


def error_404(request, not_found):
    return render(request, "Pagina_principal/404.html")


def general(request):
    num_usuarios = Usuario.objects.count()
    usuarios_done = Usuario.objects.filter(avance=5).count()
    context = {"num_usuarios": num_usuarios, "usuarios_done": usuarios_done}
    return render(request, "dashboard/general.html", context)


def usuarios(request):
    return render(request, "dashboard/usuarios.html")


def entregas(request):
    return render(request, "dashboard/entregas.html")


def opcion(request):
    return render(request, "dashboard/opcion.html")


def usuarioGraph(request, usuario_id):
    usuario = Usuario.objects.get(usuarioID=usuario_id)
    # Convierte el modelo a un diccionario y luego a JSON
    usuario_json = {
        "ID": usuario.usuarioID,
        "nombre": usuario.nombre,
        "email": usuario.email,
    }
    return render(request, "dashboard/usuario.html", usuario_json)
