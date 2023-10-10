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


@csrf_exempt
def usuarios(request):

    query = request.GET.get("busueda")
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query)
            | Q(usuarioID__icontains=query)
            | Q(contrasenia__icontains=query)
            | Q(email__icontains=query)
            | Q(avance__icontains=query)
            | Q(genero__icontains=query)
            | Q(edad__icontains=query)
            | Q(pais__icontains=query)
            | Q(institucion__icontains=query)
            | Q(grado__icontains=query)
            | Q(diciplina__icontains=query)
        ).order_by("usuarioID")
        filtro = True
    else:
        usuarios = Usuario.objects.all().order_by("usuarioID")
        filtro = False
    return render(
        request,
        "dashboard/usuarios.html",
        {"usuarios": usuarios, "filtro": filtro},
    )


def entregas(request):
    return render(request, "dashboard/entregas.html")


def cambios(request):
    return render(request, "dashboard/cambios.html")


def usuarioGraph(request, usuario_id):
    usuario = Usuario.objects.get(usuarioID=usuario_id)
    # Convierte el modelo a un diccionario y luego a JSON
    usuario_json = {
        "ID": usuario.usuarioID,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "user": "user@tec.mx",
        "responses": [
            {"answer": 1, "question": {"id": 1}},
            {"answer": 1, "question": {"id": 2}},
            {"answer": 1, "question": {"id": 3}},
            {"answer": 1, "question": {"id": 4}},
            {"answer": 1, "question": {"id": 5}},
            {"answer": 1, "question": {"id": 6}},
            {"answer": 1, "question": {"id": 7}},
            {"answer": 1, "question": {"id": 8}},
            {"answer": 1, "question": {"id": 9}},
            {"answer": 1, "question": {"id": 10}},
            {"answer": 1, "question": {"id": 11}},
            {"answer": 1, "question": {"id": 12}},
            {"answer": 1, "question": {"id": 13}},
            {"answer": 1, "question": {"id": 14}},
            {"answer": 1, "question": {"id": 15}},
            {"answer": 1, "question": {"id": 16}},
            {"answer": 1, "question": {"id": 17}},
            {"answer": 1, "question": {"id": 18}},
            {"answer": 1, "question": {"id": 19}},
            {"answer": 1, "question": {"id": 20}},
            {"answer": 1, "question": {"id": 21}},
            {"answer": 1, "question": {"id": 22}},
            {"answer": 1, "question": {"id": 23}},
            {"answer": 1, "question": {"id": 24}},
        ],
    }
    return render(request, "dashboard/usuario.html", usuario_json)
