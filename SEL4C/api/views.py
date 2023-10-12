"""Views (Logic) for API calls."""
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

from .models import (
    Usuario,
    Admin,
    Actividad,
    CuestionarioInicial,
    CuestionarioFinal,
    CambioNombre,
    CambioContrasenia,
)
from .serializer import (
    AdminSerialiizer,
    UsuarioSerializer,
    ActividadSerializer,
    CuestionarioISerializer,
    CuestionarioFSerializer,
    CambioNombreSerializer,
    CambioContraseniaSerializer,
)
from .forms import (
    AdminForm,
    UsuarioForm,
    ActividadForm,
    CuestionarioIForm,
    CuestionarioFForm,
    CambioNForm,
    CambioCForm,
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


class CuestionarioFViewSet(viewsets.ModelViewSet):
    """Creación de cuestionarios finales dentro de la base de datos."""

    queryset = CuestionarioFinal.objects.all()
    serializer_class = CuestionarioFSerializer


class CambioNViewSet(viewsets.ModelViewSet):
    """Creación de solicitudes de cambio de nombre dentro de la base de datos."""

    queryset = CambioNombre.objects.all()
    serializer_class = CambioNombreSerializer


class CambioCViewSet(viewsets.ModelViewSet):
    """Creación de solicitudes de cambio de contrasenia dentro de la base de datos."""

    queryset = CambioContrasenia.objects.all()
    serializer_class = CambioContraseniaSerializer


def crearActividad(actividad):
    actividad_serializer = ActividadSerializer(actividad)


def crearUsuario(usuario):
    usuario_serializer = UsuarioSerializer(usuario)


def crearSolicitudN(solicitud):
    solicitudN_serializer = CambioNombreSerializer


def crearSolicitudC(solicitud):
    solicitudC_serializer = CambioContraseniaSerializer


def crearRespuestasI(solicitud):
    cuestionarioI_serializer = CuestionarioISerializer


def crearRespuestasF(solicitud):
    cuestionarioF_serializer = CuestionarioFSerializer


# Función para subir archivos al proyecto de Django (por si fuera a ser necesario)
def acrchivo_subido(f):
    with open("static/upload/" + f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def validar_user(name, password):
    try:
        usuario = Usuario.objects.get(nombre=name, contrasenia=password)
        usuarioID = usuario.usuarioID
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


"""
@csrf_exempt
def index(request):
    return render(request, "Pagina_principal/index.html")


@csrf_exempt
def descargar_app(request):
    return render(request, "Pagina_principal/descargar.html")



@csrf_exempt
def error_404(request, not_found):
    return render(request, 'Pagina_principal/404.html')
"""

"""
@csrf_exempt
def existe_admin(request):
    Revisa si el usuario existe en la base de datos.

    if request.method == "POST":
        nombre = request.POST.get("nombre", False)
        contrasenia = request.POST.get("contrasenia", False)
        admin_id = validar_admin(nombre, contrasenia)
        if admin_id is not None:
            print("si?")
            return HttpResponseRedirect("/dashboard/general")
        else:
            return render(request, "Pagina_principal/iniciar_sesion.html")
"""


@csrf_exempt
def existe_usuario(request):
    """Revisa si el usuario existe en la base de datos."""
    if request.method == "POST":
        try:
            data = loads(request.body)

            email = data["email"]
            contrasenia = data["contrasenia"]

            usuario = Usuario.objects.get(email=email, contrasenia=contrasenia)
            usuarioID = usuario.usuarioID
            nombre = usuario.nombre
            avance = usuario.avance

            return JsonResponse(
                {
                    "status": "existe",
                    "nombre": nombre,
                    "contrsenia": contrasenia,
                    "usuarioID": usuarioID,
                    "avance": avance,
                    "email": email,
                }
            )
        except:
            return JsonResponse({"status": "no existe"})


"""
@csrf_exempt
def admin_login(request):
      End point para validar el admin
    return render(request, "Pagina_principal/iniciar_sesion.html")
"""


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
def enviar_solicitudN(request):
    if request.method == "POST":
        try:
            data = loads(request.body)

            nombre = data["nombre"]
            estatus = data["estatus"]
            usuarioID = data["usuarioID"]

            solicitud = CambioNombre.objects.create(
                nombre=nombre,
                estatus=estatus,
                usuarioID=usuarioID,
            )
            crearSolicitudN(solicitud)

            return JsonResponse({"message": "Solicitud Enviada"})
        except:
            return JsonResponse({"error": "Ha ocurrido un errror :("}, status=400)


@csrf_exempt
def enviar_solicitudC(request):
    if request.method == "POST":
        try:
            data = loads(request.body)

            contrasenia = data["contrasenia"]
            estatus = data["estatus"]
            usuarioID_id = data["usuarioID_id"]

            elUsario = Usuario.objects.get(usuarioID=usuarioID_id)

            solicitud = CambioContrasenia.objects.create(
                contrasenia=contrasenia,
                estatus=estatus,
                usuarioID=elUsario,
            )
            crearSolicitudC(solicitud)

            return JsonResponse({"message": "Solicitud Enviada"})
        except:
            return JsonResponse({"error": "Ha ocurrido un errror :("}, status=400)


@csrf_exempt
def repuestas_cuestionarioI(request):
    if request.method == "POST":
        data = loads(request.body)
        usuario_id = data["usuarioID"]
        responses = data["responses"]
        try:
            usuario = Usuario.objects.get(usuarioID=usuario_id)
        except Usuario.DoesNotExist:
            return JsonResponse({"message": "Usuario does not exist."})

        for response in responses:
            answer = response.get("answer")
            response_id = response.get("id")

            CuestionarioInicial.objects.create(
                preguntaID=response_id, respuesta=answer, usuarioID=usuario
            )

        return JsonResponse({"message": "Data processed successfully."}, status=200)
    return JsonResponse({"message": "Invalid request method."}, status=405)


@csrf_exempt
def repuestas_cuestionarioF(request):
    if request.method == "POST":
        try:
            data = loads(request.body)

            numero = data["numero"]
            respuesta = data["respuesta"]
            usuarioID_id = data["usuarioID_id"]

            elUsario = Usuario.objects.get(usuarioID=usuarioID_id)

            solicitud = CuestionarioFinal.objects.create(
                numero=numero,
                respuesta=respuesta,
                usuarioID=elUsario,
            )
            crearRespuestasF(solicitud)

            return JsonResponse({"message": "Solicitud Enviada"})
        except:
            return JsonResponse({"error": "Ha ocurrido un errror :("}, status=400)


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


## CRUD general ##
# CRUD admins


@csrf_exempt
def ver_admins(request):

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
        request, "CRUD_Admin/ver_admins.html", {"admins": admins, "filtro": filtro}
    )


@csrf_exempt
def actulizar_admins(request, pk):
    admin = get_object_or_404(Admin, pk=pk)

    if request.method == "POST":
        form = AdminForm(request.POST, instance=admin)
        print(form)
        if form.is_valid():
            form.save()
            print("Exito")
            return redirect("ver_admins")
        else:
            error_messages = form.errors.values()
            for error in error_messages:
                print(error)
                return redirect("ver_admins")
    else:
        form = AdminForm(instance=admin)
        return render(request, "dashboard/admins.html", {"form": form})


@csrf_exempt
def borrar_admins(request, adminID):
    admin = get_object_or_404(Admin, pk=adminID)
    admin.delete()
    print("Exito")
    return redirect("ver_admins")


@csrf_exempt
def crear_Admin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_admins")
        else:

            error_message = form.errors.values()
            for error in error_message:
                print(error)

            return redirect("crear_Admin")
    else:
        form = AdminForm()
    return render(request, "CRUD_Admin/crear_admins.html", {"form": form})


# CRUD usuarios
@csrf_exempt
def ver_usuarios(request):

    query = request.GET.get("busueda")
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query)
            | Q(contrasenia__icontains=query)
            | Q(email__icontains=query)
            | Q(avance__icontains=query)
            | Q(genero__icontains=query)
            | Q(edad__icontains=query)
            | Q(pais__icontains=query)
            | Q(institucion__icontains=query)
            | Q(grado__icontains=query)
            | Q(diciplina__icontains=query)
        ).order_by("nombre", "contrasenia")
        filtro = True
    else:
        usuarios = Usuario.objects.all().order_by("nombre")
        filtro = False

    """ ver si se usaran sesiones o cookies
    exito = request.session.pop('exito', None)

    error = request.session.pop('error', None)
    """

    return render(
        request,
        "CRUD_Usuarios/ver_usuarios.html",
        {"usuarios": usuarios, "filtro": filtro},
    )


@csrf_exempt
def ver_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    return render(request, "CRUD_Usuarios/ver_usuario.html", {"usuario": usuario})


@csrf_exempt
def actualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, usuarioID=pk)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
        else:
            error_messages = form.errors.values()
            for error in error_messages:
                print(error)
                return redirect("usuarios")
    else:
        form = UsuarioForm(instance=usuario)
        return render(request, "dashboard/usuarios.html", {"form": form})


@csrf_exempt
def borrar_usuarios(request, usuarioID):
    usuario = get_object_or_404(Usuario, pk=usuarioID)
    usuario.delete()
    print("Exito")
    return redirect("SEL4C_Dashboard/usuarios")


@csrf_exempt
def crear_Usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_usuarios")
        else:
            error_message = form.errors.values()
            for error in error_message:
                print(error)

            return redirect("ver_usuarios")
    else:
        form = UsuarioForm()
    return render(request, "dashboard/usuarios.html", {"form": form})


# CRUD actividades
def ver_actividades(request):

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
        "CRUD_Actividades/ver_actividades.html",
        {"actividades": actividades, "filtro": filtro},
    )


# CRUD encuestas


def ver_ecnuestasI(request):
    query = request.GET.get("busqueda")
    if query:
        encuestasI = CuestionarioInicial.objects.filter(
            Q(numero__icontains=query)
            | Q(respuesta__icontains=query)
            | Q(usuarioID_id__icontains=query)
        ).order_by("numero", "respuesta")
        filtro = True
    else:
        encuestasI = CuestionarioInicial.objects.all().order_by("numero")
        filtro = False

    return render(
        request,
        "CRUD_Encuestas/ver_encuestaI.html",
        {"encuestasI": encuestasI, "filtro": filtro},
    )


def ver_ecnuestasF(request):
    query = request.GET.get("busqueda")
    if query:
        encuestasF = CuestionarioFinal.objects.filter(
            Q(numero__icontains=query)
            | Q(respuesta__icontains=query)
            | Q(usuarioID_id__icontains=query)
        ).order_by("numero", "respuesta")
        filtro = True
    else:
        encuestasF = CuestionarioFinal.objects.all().order_by("numero")
        filtro = False

    return render(
        request,
        "CRUD_Encuestas/ver_encuestosF.html",
        {"encuestasf": encuestasF, "filtro": filtro},
    )


# CRUD solicitudes de cambio


def ver_solicitudes_nombres(request):
    query = request.GET.get("busqueda")
    if query:
        solicitudesN = CambioNombre.objects.filter(
            Q(nombre__icontains=query)
            | Q(estatus__icontains=query)
            | Q(usuarioID_id__icontains=query)
        ).order_by("nombre", "estatus")
        filtro = True
    else:
        solicitudesN = CambioNombre.objects.all().order_by("solicitudNID")
        filtro = False

    return render(
        request,
        "CRUD_Solicitudes/ver_solicitudes_nombre.html",
        {"solicitudesN": solicitudesN, "filtro": filtro},
    )


def cambiar_nombre(request, usuarioID_id, nombre, solicitudNID):
    usuario = get_object_or_404(Usuario, pk=usuarioID_id)
    usuario.nombre = nombre
    usuario.save()

    solicitud = CambioNombre.objects.get(solicitudNID=solicitudNID)
    solicitud.estatus = "Resuelto"
    solicitud.save()

    print("Exito")
    return redirect("ver_solicitudes_nombres")


def ver_solicitudes_contrasenia(request):
    query = request.GET.get("busqueda")
    if query:
        solicitudesC = CambioContrasenia.objects.filter(
            Q(contrasenia__icontains=query)
            | Q(estatus__icontains=query)
            | Q(usuarioID_id__icontains=query)
        ).order_by("contrasenia", "estatus")
        filtro = True
    else:
        solicitudesC = CambioContrasenia.objects.all().order_by("solicitudCID")
        filtro = False

    return render(
        request,
        "CRUD_Solicitudes/ver_solicitudes_contrasenia.html",
        {"solicitudesC": solicitudesC, "filtro": filtro},
    )


def cambiar_contrasenia(request, usuarioID_id, contrasenia, solicitudCID):
    usuario = get_object_or_404(Usuario, pk=usuarioID_id)
    usuario.contrasenia = contrasenia
    usuario.save()

    solicitud = CambioContrasenia.objects.get(solicitudCID=solicitudCID)
    solicitud.estatus = "Resuelto"
    solicitud.save()

    print("Exito")
    return redirect("ver_solicitudes_contrasenia")
