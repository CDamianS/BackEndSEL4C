from django.db import models


# Create your models here.
# Parametos para el model de Actividades


usuario_genero = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
    ("Prefiero no decir", "Prefiero no decirlo")
)
grado_academico = (
    ("Pregrado (licenciatura, profesional, universidad, grado)", "Pregrado (licenciatura, profesional, universidad, grado)"),
    ("Posgrado (maestría, doctorado)", "Posgrado (maestría, doctorado)"),
    ("Educación continua", "Educación continua")
)
disciplina_c = (
    ("Ingenieria y ciencias", "Ingenieria y ciencias"),
    ("Humanidades y ciencia", "Humanidades y ciencia"),
    ("Ciencias sociales", "Ciencias sociales"),
    ("Ciencias de la salud", "Ciencias de la salud"),
    ("Arquitectura, Arte y Diseño", "Arquitectura, Arte y Diseño"),
    ("Negocios", "Negocios")
)

class Usuario(models.Model):
    usuarioID = models.AutoField(primary_key=True, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    contrasenia = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    avance = models.IntegerField(default=0)
    genero = models.CharField(max_length=50, blank=True, choices=usuario_genero)
    edad = models.IntegerField(blank=True)
    pais = models.CharField(max_length=50, blank=True)
    institucion = models.CharField(max_length=100, blank=True, default = "Tecnológico de Monterrey")
    grado = models.CharField(max_length=100, blank=True, choices=grado_academico)
    diciplina = models.CharField(max_length=100, blank=True, choices=disciplina_c)
    respuestasI = models.BooleanField(default=False)

    def __str__(self):
        return f"Usuario {self.usuarioID}: {self.nombre}"

        # return f'Usuario {self.usuarioID}: {self.nombre} - Email: {self.email} - Avance: {self.avance} - Genero: {self.genero} - Edad: {self.genero} - Pais: {self.pais} - Institucion: {self.institucion} - Grado: {self.grado} - Diciplina: {self.diciplina}'


class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    contrasenia = models.CharField(max_length=50)

    def __str__(self):
        return f"Admin {self.adminID}: {self.nombre}"


class Actividad(models.Model):
    actividadID = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=100
    )
    estatus = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    usuarioID = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    entregable = models.FileField(default=None)

    def __str__(self):
        return f"Actividad {self.actividadID}: {self.nombre} - Estatus: {self.estatus} - Usuario: {self.usuarioID} - Entregable: {self.entregable}"


class CuestionarioInicial(models.Model):
    preguntaID = models.AutoField(primary_key=True)
    numero = models.IntegerField(default=0)
    respuesta = models.CharField(max_length=50)
    usuarioID = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f"Pregunta {self.numero} - Respuesta: {self.respuesta} - Usuario: {self.usuarioID}"


class CuestionarioFinal(models.Model):
    preguntaID = models.AutoField(primary_key=True)
    numero = models.IntegerField(default=0)
    respuesta = models.CharField(max_length=50)
    usuarioID = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return f'Pregunra {self.numero} - Respuesta: {self.respuesta} - Usuario: {self.usuarioID}'
    

class CambioNombre(models.Model):
    solicitudNID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    usuarioID = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    estatus = models.CharField(max_length=50)

    def __str__(self):
        return f'Solicitud {self.solicitudNID} - Nuevo nombre: {self.nombre} - Usuario: {self.usuarioID} - Estatus: {self.estatus}'
    

class CambioContrasenia(models.Model):
    solicitudCID = models.AutoField(primary_key=True)
    contrasenia = models.CharField(max_length=50)
    usuarioID = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    estatus = models.CharField(max_length=50)

    def __str__(self):
        return f'Solicitud {self.solicitudNID} - Nueva contrasenia: {self.contrasenia} - Usuario: {self.usuarioID} - Estatus: {self.estatus}'

