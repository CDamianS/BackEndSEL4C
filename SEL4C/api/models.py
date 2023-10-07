from django.db import models

# Create your models here.

# Parametos para el model de Actividades
estatus_status = ["Completado", "No completado"]
nombre_status = [
    "1.- Identificación",
    "2.- Investigación",
    "3.- Ideación",
    "4.- Socialización",
    "Entregable final",
]


class Usuario(models.Model):
    usuarioID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    avance = models.IntegerField()
    genero = models.CharField(max_length=20)
    edad = models.IntegerField()
    pais = models.CharField(max_length=50)
    institucion = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    diciplina = models.CharField(max_length=100)

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
    nombre = models.CharField(max_length=100)
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
        return f"Pregunta {self.numero} - Respuesta: {self.respuesta} - Usuario: {self.usuarioID}"
