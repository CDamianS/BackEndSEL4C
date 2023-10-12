from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from json import loads, dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from api.models import Usuario
import requests
from django.db.models import Q
from api.models import (
    Usuario,
    Admin,
    Actividad,
    CuestionarioInicial,
    CuestionarioFinal,
    CambioNombre,
    CambioContrasenia,
)
from api.serializer import (
    AdminSerialiizer,
    UsuarioSerializer,
    ActividadSerializer,
    CuestionarioISerializer,
    CuestionarioFSerializer,
    CambioNombreSerializer,
    CambioContraseniaSerializer,
)
from api.forms import (
    AdminForm,
    UsuarioForm,
    ActividadForm,
    CuestionarioIForm,
    CuestionarioFForm,
    CambioNForm,
    CambioCForm,
)

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

    query = request.GET.get("busueda")
    if query:
        actividades = Actividad.objects.filter(
            Q(nombre__icontains=query) | Q(usuarioID_id__icontains=query)
        ).order_by("nombre", "usuarioID_id_")
        filtro = True
    else:
        actividades = Actividad.objects.all().order_by("nombre")
        filtro = False

    """ ver si se usaran sesiones o cookies
    exito = request.session.pop('exito', None)

    error = request.session.pop('error', None)
    """

    return render(
        request,
        "dashboard/entregas.html",
        {"actividades": actividades, "filtro": filtro},
    )


def cambios(request):
    solicitudesN = CambioNombre.objects.all().order_by("solicitudNID")
    solicitudesC = CambioContrasenia.objects.all().order_by("solicitudCID")
    return render(
        request,
        "dashboard/cambios.html",
        {"solicitudesN": solicitudesN, "solicitudesC": solicitudesC},
    )


def administradores(request):
    query = request.GET.get("busueda")
    if query:
        admins = Admin.objects.filter(
            Q(nombre__icontains=query) | Q(contrasenia__icontains=query)
        ).order_by("nombre", "contrasenia")
        filtro = True
    else:
        admins = Admin.objects.all().order_by("nombre")
        filtro = False

    """ ver si se usaran sesiones o cookies
    exito = request.session.pop('exito', None)

    error = request.session.pop('error', None)
    """

    return render(
        request, "dashboard/admins.html", {"admins": admins, "filtro": filtro}
    )


def usuarioGraph(request, usuario_id):
    usuario = Usuario.objects.get(usuarioID=usuario_id)
    usuario_json = {
        "nombre": usuario.nombre,
        "email": usuario.email,
        "ID": usuario.usuarioID,
    }
    # Convierte el modelo a un diccionario y luego a JSON
    return render(request, "dashboard/usuario.html", usuario_json)
