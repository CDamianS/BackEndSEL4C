from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import loads, dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
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
    return render(request, "dashboard/general.html")


def usuarios(request):
    return render(request, "dashboard/usuarios.html")


def entregas(request):
    return render(request, "dashboard/entregas.html")


def opcion(request):
    return render(request, "dashboard/opcion.html")
