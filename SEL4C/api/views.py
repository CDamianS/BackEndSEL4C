"""Views (Logic) for API calls."""
from django.http import JsonResponse
from SEL4C_Dashboard.models import (
    Usuario,
    Admin,
    Actividad,
    CuestionarioInicial,
    CuestionarioFinal,
)


def register_usuario(request):
    """Register user inside of the db."""
    if request.method == "POST":
        usuarioID = request.POST.get("usuario")
        nombre = request.POST.get("nombre")
        contrasenia = request.POST.get("contrasenia")
        email = request.POST.get("email")
        # TODO: revisar formato de avance
        avance = request.POST.get("avance")
        genero = request.POST.get("genero")
        edad = request.POST.get("edad")
        pais = request.POST.get("pais")
        institucion = request.POST.get("institucion ")
        grado = request.POST.get("grado")
        diciplina = request.POST.get("diciplina")
        user = Usuario.objects.create(
            usuarioID=usuarioID,
            nombre=nombre,
            contrasenia=contrasenia,
            email=email,
            avance=avance,
            genero=genero,
            edad=edad,
            pais=pais,
            institucion=institucion,
            grado=grado,
            diciplina=diciplina,
        )
        user.save()
        return JsonResponse({"status": "success"})


def validar_usario(request):
    """Validate user inside of the db."""
    if request.method == 'POST':
        userid = request.POST.get('usuario')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(usuarioID=userid)
            # TODO: actual authentication
            if password == usuario.password():
                return JsonResponse({'status': 'success',
                                     'message': 'Usuario validado'})
        except Usuario.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'El usuario no existe'})


def cuestionario_inicial(request):
    """Send the initial questions"""
    questions = [{"id": 1,
        "text": "Cuando algo me apasiona hago lo posible para lograr mis metas."},
    {"id": 2,
        "text": "Cuando mi trabajo me apasiona hago lo posible por concluirlo, aunque enfrente circunstancias adversas, falta de tiempo o distractores."},
    {"id": 3,
        "text": "A pesar del rechazo o problemas, siempre busco conseguir mis objetivos."},
    {"id": 4,
        "text": "Soy tolerante ante situaciones ambiguas o que me generen incertidumbre."},
    {"id": 5,
        "text": "Tengo la capacidad de establecer una meta clara y los pasos para lograrla."},
    {"id": 6,
        "text": "Es común que logre convencer a otros sobre mis ideas y acciones."},
    {"id": 7,
        "text": "Domino diferentes formas de comunicar mis ideas: por escrito, en un video o en charlas cara a cara."},
    {"id": 8,
        "text": "Se me facilita delegar actividades a los miembros de mi equipo de acuerdo con sus perfiles."},
    {"id": 9,
        "text": "Tengo la habilidad de identificar las fortalezas y debilidades de las personas con las que trabajo."},
    {"id": 10,
        "text": " Se me facilita colaborar de manera activa en un equipo para lograr objetivos comunes."},
    {"id": 11,
        "text": " Me apasiona trabajar en favor de causas sociales."},
    {"id": 12,
        "text": " Creo que la misión de mi vida es trabajar para el cambio social y mejorar la vida de las personas."},
    {"id": 13,
        "text": " Me interesa dirigir una iniciativa con resultados favorables para la sociedad y/o el medio ambiente."},
    {"id": 14,
        "text": " Soy capaz de identificar problemas en el entorno social o ambiental para generar soluciones innovadoras."},
    {"id": 15,
        "text": " Manifiesto un compromiso por participar en aspectos sociales de mi entorno."},
    {"id": 16,
        "text": " Opino que el crecimiento económico debe ocurrir en igualdad de oportunidades y equidad para todos."},
    {"id": 17,
        "text": " Mis acciones y comportamientos se rigen por normas morales basadas en el respeto y cuidado hacia las personas y a la naturaleza."},
    {"id": 18,
        "text": " Sé cómo aplicar estrategias para crear nuevas ideas o proyectos."},
    {"id": 19,
        "text": " Sé aplicar conocimientos contables y financieros para el desarrollo de un emprendimiento."},
    {"id": 20,
        "text": " Tengo nociones sobre la logística para llevar a cabo la gestión de una organización."},
    {"id": 21,
        "text": " Sé cómo realizar un presupuesto para lograr un proyecto."},
    {"id": 22,
        "text": " Sé cómo establecer criterios de valoración y medir los resultados de impacto social."},
    {"id": 23,
        "text": " Creo que el cometer errores nos ofrece nuevas oportunidades de aprendizaje."},
    {"id": 24,
        "text": " Conozco estrategias para desarrollar un proyecto, aún con escasez de recursos."},
        ]
    return JsonResponse(questions, safe=False)
