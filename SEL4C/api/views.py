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
