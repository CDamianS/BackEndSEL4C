"""Views (Logic) for API calls."""
from django.http import JsonResponse
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import loads, dumps, JSONDecodeError, JSONDecoder, load
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import requests
from django.core.files.storage import FileSystemStorage
import os

from .models import (
    Usuario,
    Admin,
    Actividad,
    CuestionarioInicial,
    CuestionarioFinal,
)
from .serializer import (
    AdminSerialiizer,
    UsuarioSerializer,
    ActividadSerializer,
    CuestionarioISerializer,
    CuestionarioFSerializer,
)
from .forms import (
    AdminForm,
    UsuarioForm,
    ActividadForm,
    CuestionarioIForm,
    CuestionarioFForm,
)


class AdminViewSet(viewsets.ModelViewSet):
    """Creación de admins dentro de la base de datos."""

    queryset = Admin.objects.all()
    serializer_class = AdminSerialiizer


class UserViewSet(viewsets.ModelViewSet):
    """Creación de usuarios dentro de la base de datos."""

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    """Creación de actividades dentro de la base de datos."""

    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer


class CuestionarioIViewSet(viewsets.ModelViewSet):
    """Creación de cuestionarios iniciales dentro de la base de datos."""

    queryset = CuestionarioInicial.objects.all()
    serializer_class = CuestionarioISerializer


def crearActividad(actividad):
    actividad_serializer = ActividadSerializer(actividad)


def crearUsuario(usuario):
    usuario_serializer = UsuarioSerializer(usuario)


# Función para subir archivos al proyecto de Django (por si fuera a ser necesario)
def acrchivo_subido(f):
    with open("static/upload/" + f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def validar_user(name, password):
    try:
        user = Usuario.objects.get(nombre=name, contrasenia=password)
        user_ID = user.userID
    except:
        user_ID = None
    return user_ID


@csrf_exempt
def validar_admin(name, password):
    try:
        admin = Admin.objects.get(nombre=name, contrasenia=password)
        admin_id = admin.adminID
    except:
        admin_id = None
    return admin_id


@csrf_exempt
def selecionar_actividad(idAct, idUser):
    try:
        actividad = Actividad.objects.get(actividadID=idAct, usuarioID=idUser)
        actividad_id = actividad.usuarioID
    except:
        actividad_id = None
    return actividad_id


@csrf_exempt
def index(request):
    return render(request, "Pagina_principal/index.html")


@csrf_exempt
def descargar_app(request):
    return render(request, "Pagina_principal/descargar.html")


"""
@csrf_exempt
def error_404(request, not_found):
    return render(request, 'Pagina_principal/404.html')
"""


@csrf_exempt
def existe_admin(request):
    """Revisa si el usuario existe en la base de datos."""

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        admin_id = validar_admin(username, password)
        if admin_id is not None:
            print("si?")
            return render(request, "dashboard_base.html")
        else:
            return HttpResponseRedirect("//url1/")
            # return render(request, "Pagina_principal/iniciar_sesion.html")


@csrf_exempt
def existe_usuario(request):
    """Revisa si el usuario existe en la base de datos."""

    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]
        User_ID = validar_user(name, password)

        if User_ID is None:
            return JsonResponse({"status": "no existe"})
        else:
            return JsonResponse({"status": "existe"})


@csrf_exempt
def crear_Admin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ok!!!")
        else:

            error_message = form.errors.values()
            for error in error_message:
                print(error)

            return HttpResponse("erorr :(")
    else:
        form = AdminForm()
    return render(request, "admin_creacion(prueb).html", {"form": form})


@csrf_exempt
def admin_login(request):
    """End point para validar el admin"""
    return render(request, "Pagina_principal/iniciar_sesion.html")


@csrf_exempt
def user_login(request):
    """End point para validar el usuario"""
    return render(request, "user_login.html")


@csrf_exempt
def creacion_usuario(request):
    if request.method == "POST":
        try:
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Registro Exitoso"})
            else:

                error_message = form.errors.values()
                for error in error_message:
                    print(error)

                return JsonResponse({"message": "Erorr en los datos de registro"})
        except:
            return JsonResponse({"message": "Erorr en los datos de registro"})
    else:
        return HttpResponse("Error en el metodo de requets")


@csrf_exempt
def upload(request):
    if request.method == "POST":
        try:
            data = request.POST
            file = request.FILES

            nombre = data["nombre"]
            estatus = data["estatus"]
            usuarioID = data["usuarioID"]
            entregable = file["entregable"]

            elUsuario = Usuario.objects.get(usuarioID=usuarioID)
            elUsuario.avance += 1
            elUsuario.save()

            actividad = Actividad.objects.create(
                nombre=nombre,
                estatus=estatus,
                usuarioID=elUsuario,
                entregable=entregable,
            )
            crearActividad(actividad)

            return JsonResponse({"message": "La actividad se entrgo correctamente!!!"})
        except:
            return JsonResponse({"error": "Ha ocurrido un errror :("}, status=400)
    else:
        return HttpResponse("Error en el metodo de requet")


@csrf_exempt
def download(request, file_id):
    try:
        file = Actividad.objects.get(pk=file_id)
        response = HttpResponse(
            file.entregable, content_type="application/force-download"
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{file.entregable.name}"'
        return response
    except:
        return HttpResponse("Este archivo no existe en la base de datos")


@csrf_exempt
def repuestas_cuestionario(request):
    if request.method == "POST":
        data = request.POST

        usuarioID = data["usuarioID"]

        print(usuarioID)

        return HttpResponse("si")

    return HttpResponse("??")


@csrf_exempt
def cuestionario_inicial(request):
    """Send the initial questions."""
    questions = [
        {
            "id": 1,
            "text": "Cuando algo me apasiona hago lo posible para lograr mis metas.",
        },
        {
            "id": 2,
            "text": "Cuando mi trabajo me apasiona hago lo posible por concluirlo, aunque enfrente circunstancias adversas, falta de tiempo o distractores.",
        },
        {
            "id": 3,
            "text": "A pesar del rechazo o problemas, siempre busco conseguir mis objetivos.",
        },
        {
            "id": 4,
            "text": "Soy tolerante ante situaciones ambiguas o que me generen incertidumbre.",
        },
        {
            "id": 5,
            "text": "Tengo la capacidad de establecer una meta clara y los pasos para lograrla.",
        },
        {
            "id": 6,
            "text": "Es común que logre convencer a otros sobre mis ideas y acciones.",
        },
        {
            "id": 7,
            "text": "Domino diferentes formas de comunicar mis ideas: por escrito, en un video o en charlas cara a cara.",
        },
        {
            "id": 8,
            "text": "Se me facilita delegar actividades a los miembros de mi equipo de acuerdo con sus perfiles.",
        },
        {
            "id": 9,
            "text": "Tengo la habilidad de identificar las fortalezas y debilidades de las personas con las que trabajo.",
        },
        {
            "id": 10,
            "text": " Se me facilita colaborar de manera activa en un equipo para lograr objetivos comunes.",
        },
        {"id": 11, "text": " Me apasiona trabajar en favor de causas sociales."},
        {
            "id": 12,
            "text": " Creo que la misión de mi vida es trabajar para el cambio social y mejorar la vida de las personas.",
        },
        {
            "id": 13,
            "text": " Me interesa dirigir una iniciativa con resultados favorables para la sociedad y/o el medio ambiente.",
        },
        {
            "id": 14,
            "text": " Soy capaz de identificar problemas en el entorno social o ambiental para generar soluciones innovadoras.",
        },
        {
            "id": 15,
            "text": " Manifiesto un compromiso por participar en aspectos sociales de mi entorno.",
        },
        {
            "id": 16,
            "text": " Opino que el crecimiento económico debe ocurrir en igualdad de oportunidades y equidad para todos.",
        },
        {
            "id": 17,
            "text": " Mis acciones y comportamientos se rigen por normas morales basadas en el respeto y cuidado hacia las personas y a la naturaleza.",
        },
        {
            "id": 18,
            "text": " Sé cómo aplicar estrategias para crear nuevas ideas o proyectos.",
        },
        {
            "id": 19,
            "text": " Sé aplicar conocimientos contables y financieros para el desarrollo de un emprendimiento.",
        },
        {
            "id": 20,
            "text": " Tengo nociones sobre la logística para llevar a cabo la gestión de una organización.",
        },
        {"id": 21, "text": " Sé cómo realizar un presupuesto para lograr un proyecto."},
        {
            "id": 22,
            "text": " Sé cómo establecer criterios de valoración y medir los resultados de impacto social.",
        },
        {
            "id": 23,
            "text": " Creo que el cometer errores nos ofrece nuevas oportunidades de aprendizaje.",
        },
        {
            "id": 24,
            "text": " Conozco estrategias para desarrollar un proyecto, aún con escasez de recursos.",
        },
    ]
    return JsonResponse(questions, safe=False)


def cuestionario_PC(request):
    """Send the initial questions."""
    questions = [
        {
            "id": 1,
            "text": " Creo que el cometer errores nos ofrece nuevas oportunidades de aprendizaje.",
        },
        {
            "id": 2,
            "text": "Identifico datos de mi disciplina y de otras áreas que contribuyen a resolver problemas.",
        },
        {
            "id": 3,
            "text": "Participo en proyectos que se tienen que resolver utilizando perspectivas Inter/multidisciplinarias.",
        },
        {
            "id": 4,
            "text": "Organizo información para resolver problemas.",
        },
        {
            "id": 5,
            "text": "Me agrada conocer perspectivas diferentes de un problema.",
        },
        {
            "id": 6,
            "text": "Me inclino por estrategias para comprender las partes y el todo de un problema.",
        },
        {
            "id": 7,
            "text": "Tengo la capacidad de Identificar los componentes esenciales de un problema para formular una pregunta de investigación.",
        },
        {
            "id": 8,
            "text": "Conozco la estructura y los formatos para elaborar reportes de investigación que se utilizan en mi área o disciplina.",
        },
        {
            "id": 9,
            "text": "Identifico la estructura de un artículo de investigación que se maneja en mi área o disciplina.",
        },
        {
            "id": 10,
            "text": "Identifico los elementos para formular una pregunta de investigación.",
        },
        {
            "id": 11,
            "text": "Diseño instrumentos de investigación coherentes con el método de investigación utilizado.",
        },
        {
            "id": 12,
            "text": "Formulo y pruebo hipótesis de investigación.",
        },
        {
            "id": 13,
            "text": "Me inclino a usar datos científicos para analizar problemas de investigación.",
        },
        {
            "id": 14,
            "text": "Tengo la capacidad para analizar críticamente problemas desde diferentes perspectivas.",
        },
        {
            "id": 15,
            "text": "Identifico la fundamentación de juicios propios y ajenos para reconocer argumentos falsos.",
        },
        {
            "id": 16,
            "text": "Autoevalúo  el nivel de avance y logro de mis metas para hacer los ajustes necesarios.",
        },
        {
            "id": 17,
            "text": "Utilizo razonamientos basados en el conocimiento científico para emitir juicios ante un problema.",
        },
        {
            "id": 18,
            "text": "Me aseguro de revisar los lineamientos éticos de los proyectos en los que participo.",
        },
        {
            "id": 19,
            "text": "Me aseguro de revisar los lineamientos éticos de los proyectos en los que participo.",
        },
        {
            "id": 20,
            "text": "Aprecio críticas en el desarrollo de proyectos para mejorarlos.",
        },
        {
            "id": 21,
            "text": "Conozco los criterios para determinar un problema.",
        },
        {
            "id": 22,
            "text": "Tengo la capacidad de identificar las variables, de diversas disciplinas, que pueden ayudar a responder preguntas.",
        },
        {
            "id": 23,
            "text": "Aplico soluciones innovadoras a diversas problemáticas.",
        },
        {
            "id": 24,
            "text": "Soluciono problemas interpretando datos de diferentes disciplinas.",
        },
        {
            "id": 25,
            "text": "Analizo problemas de investigación contemplando el contexto para crear soluciones.",
        },
    ]
    return JsonResponse(questions, safe=False)
