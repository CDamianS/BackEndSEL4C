from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from json import loads, dumps, JSONDecodeError, JSONDecoder, load
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import requests
from django.core.files.storage import FileSystemStorage
import os
from api import views
from api.models import (
    Usuario,
    Admin,
    Actividad,
    CuestionarioInicial,
    CuestionarioFinal,
    CambioNombre,
    CambioContrasenia
)
from api.serializer import (
    AdminSerialiizer,
    UsuarioSerializer,
    ActividadSerializer,
    CuestionarioISerializer,
    CuestionarioFSerializer,
    CambioNombreSerializer,
    CambioContraseniaSerializer
)
from api.forms import (
    AdminForm,
    UsuarioForm,
    ActividadForm,
    CuestionarioIForm,
    CuestionarioFForm,
    CambioNForm,
    CambioCForm
)

#Functions and classes
@csrf_exempt
def validar_admin(name, password):
    try:
        admin = Admin.objects.get(nombre=name, contrasenia=password)
        admin_id = admin.adminID
    except:
        admin_id = None
    return admin_id

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, "Pagina_principal/index.html")


@csrf_exempt
def descargar_app(request):
    return render(request, "Pagina_principal/descargar.html")

@csrf_exempt
def admin_login(request):
    """End point para validar el admin"""
    
    if not request.session.get('login'):
        
        return render(request, "Pagina_principal/iniciar_sesion.html")
    else:
        return redirect("/dashboard/general")


@csrf_exempt
def existe_admin(request):
    """Revisa si el usuario existe en la base de datos."""

    if request.method == "POST":
        nombre = request.POST.get("nombre", False)
        contrasenia = request.POST.get("contrasenia", False)
        admin_id = validar_admin(nombre, contrasenia)

        if admin_id is not None:
            request.session['login'] = True
            request.session['id'] = admin_id
            return redirect("/dashboard/general")
        else:
            return render(request, "Pagina_principal/iniciar_sesion.html")

@csrf_exempt
def logout(request):
    request.session['login'] = False
    del request.session['id']

    return redirect('admin_login')
