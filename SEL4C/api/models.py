from django.db import models
# Create your models here.
# Parametos para los modelos

paises = (
    ("Afganistán", "Afganistán"),
    ("Albania", "Albania"),
    ("Samoa Americana", "Samoa Americana"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Anguilla", "Anguilla"),
    ("Antártida", "Antártida"),
    ("Antigua y Barbuda", "Antigua y Barbuda"),
    ("Armenia", "Armenia"),
    ("Aruba", "Aruba"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Bahamas", "Bahamas"),
    ("Bahrein", "Bahrein"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Bielorrusia", "Bielorrusia"),
    ("Bélgica", "Bélgica"),
    ("Belice", "Belice"),
    ("Benín", "Benín"),
    ("Bermuda", "Bermuda"),
    ("Bután", "Bután"),
    ("Bolivia", "Bolivia"),
    ("Bosnia-Herzegovina", "Bosnia-Herzegovina"),
    ("Botswana", "Botswana"),
    ("Brasil", "Brasil"),
    ("Brunei", "Brunei"),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Camboya", "Camboya"),
    ("Camerún", "Camerún"),
    ("Canadá", "Canadá"),
    ("Cabo Verde", "Cabo Verde"),
    ("Islas Caimán", "Islas Caimán"),
    ("República Centroafricana", "República Centroafricana"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Isla de Navidad", "Isla de Navidad"),
    ("Islas Cocos", "Islas Cocos"),
    ("Colombia", "Colombia"),
    ("Comores", "Comores"),
    ("República del Congo", "República del Congo"),
    ("República Democrática del Congo", "República Democrática del Congo"),
    ("Islas Cook", "Islas Cook"),
    ("Costa Rica", "Costa Rica"),
    ("Costa de Marfíl", "Costa de Marfíl"),
    ("Croacia", "Croacia"),
    ("Cuba", "Cuba"),
    ("Chipre", "Chipre"),
    ("República Checa", "República Checa"),
    ("Dinamarca", "Dinamarca"),
    ("Djibouti", "Djibouti"),
    ("Dominica", "Dominica"),
    ("República Dominicana", "República Dominicana"),
    ("Ecuador", "Ecuador"),
    ("Egipto", "Egipto"),
    ("El Salvador", "El Salvador"),
    ("Guinea Ecuatorial", "Guinea Ecuatorial"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Etiopía", "Etiopía"),
    ("Islas Malvinas", "Islas Malvinas"),
    ("Islas Feroe", "Islas Feroe"),
    ("Fiji", "Fiji"),
    ("Finlandia", "Finlandia"),
    ("Francia", "Francia"),
    ("Guyana Francesa", "Guyana Francesa"),
    ("Polinesia Francesa", "Polinesia Francesa"),
    ("Tierras Australes y Antárticas Francesas", "Tierras Australes y Antárticas Francesas"),
    ("Gabón", "Gabón"),
    ("Gambia", "Gambia"),
    ("Georgia", "Georgia"),
    ("Alemania", "Alemania"),
    ("Ghana", "Ghana"),
    ("Gibraltar", "Gibraltar"),
    ("Grecia", "Grecia"),
    ("Groenlandia", "Groenlandia"),
    ("Granada", "Granada"),
    ("Guadalupe", "Guadalupe"),
    ("Guam", "Guam"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Guyana", "Guyana"),
    ("Haití", "Haití"),
    ("Vaticano", "Vaticano"),
    ("Honduras", "Honduras"),
    ("Hong Kong", "Hong Kong"),
    ("Hungría", "Hungría"),
    ("Islandia", "Islandia"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Irán", "Irán"),
    ("Iraq", "Iraq"),
    ("Irlanda", "Irlanda"),
    ("Israel", "Israel"),
    ("Italia", "Italia"),
    ("Jamaica", "Jamaica"),
    ("Japón", "Japón"),
    ("Jordania", "Jordania"),
    ("Kazajstán", "Kazajstán"),
    ("Kenia", "Kenia"),
    ("Kiribati", "Kiribati"),
    ("Corea del Norte", "Corea del Norte"),
    ("Corea del Sur", "Corea del Sur"),
    ("Kuwait", "Kuwait"),
    ("Kirguistán", "Kirguistán"),
    ("Laos", "Laos"),
    ("Letonia", "Letonia"),
    ("Líbano", "Líbano"),
    ("Lesotho", "Lesotho"),
    ("Liberia", "Liberia"),
    ("Libia", "Libia"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lituania", "Lituania"),
    ("Macao", "Macao"),
    ("Macedonia", "Macedonia"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malasia", "Malasia"),
    ("Maldivas", "Maldivas"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Islas Marshall", "Islas Marshall"),
    ("Martinica", "Martinica"),
    ("Mauritania", "Mauritania"),
    ("Mauricio", "Mauricio"),
    ("Mayotte", "Mayotte"),
    ("México", "México"),
    ("Estados Federados de Micronesia", "Estados Federados de Micronesia"),
    ("Moldavia", "Moldavia"),
    ("Mónaco", "Mónaco"),
    ("Mongolia", "Mongolia"),
    ("Montserrat", "Montserrat"),
    ("Marruecos", "Marruecos"),
    ("Mozambique", "Mozambique"),
    ("Myanmar", "Myanmar"),
    ("Namibia", "Namibia"),
    ("Nauru", "Nauru"),
    ("Nepal", "Nepal"),
    ("Países Bajos", "Países Bajos"),
    ("Antillas Nerlandesas", "Antillas Nerlandesas"),
    ("Nueva Caledonia", "Nueva Caledonia"),
    ("Nueva Zelanda", "Nueva Zelanda"),
    ("Nicaragua", "Nicaragua"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    ("Niue", "Niue"),
    ("Islas Norfolk", "Islas Norfolk"),
    ("Islas Marianas del Norte", "Islas Marianas del Norte"),
    ("Noruega", "Noruega"),
    ("Omán", "Omán"),
    ("Pakistán", "Pakistán"),
    ("Palau", "Palau"),
    ("Panamá", "Panamá"),
    ("Papua Nueva Guinea", "Papua Nueva Guinea"),
    ("Paraguay", "Paraguay"),
    ("Perú", "Perú"),
    ("Filipinas", "Filipinas"),
    ("Pitcairn", "Pitcairn"),
    ("Polonia", "Polonia"),
    ("Portugal", "Portugal"),
    ("Puerto Rico", "Puerto Rico"),
    ("Qatar", "Qatar"),
    ("Reunión", "Reunión"),
    ("Rumanía", "Rumanía"),
    ("Rusia", "Rusia"),
    ("Ruanda", "Ruanda"),
    ("Santa Helena", "Santa Helena"),
    ("San Kitts y Nevis", "San Kitts y Nevis"),
    ("Santa Lucía", "Santa Lucía"),
    ("San Vicente y Granadinas", "San Vicente y Granadinas"),
    ("Samoa", "Samoa"),
    ("San Marino", "San Marino"),
    ("Santo Tomé y Príncipe", "Santo Tomé y Príncipe"),
    ("Arabia Saudita", "Arabia Saudita"),
    ("Senegal", "Senegal"),
    ("Serbia", "Serbia"),
    ("Seychelles", "Seychelles"),
    ("Sierra Leona", "Sierra Leona"),
    ("Singapur", "Singapur"),
    ("Eslovaquía", "Eslovaquía"),
    ("Eslovenia", "Eslovenia"),
    ("Islas Salomón", "Islas Salomón"),
    ("Somalia", "Somalia"),
    ("Sudáfrica", "Sudáfrica"),
    ("España", "España"),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudán", "Sudán"),
    ("Sudán del Sur", "Sudán del Sur"),
    ("Surinam", "Surinam"),
    ("Swazilandia", "Swazilandia"),
    ("Suecia", "Suecia"),
    ("Suiza", "Suiza"),
    ("Siria", "Siria"),
    ("Taiwán", "Taiwán"),
    ("Tadjikistan", "Tadjikistan"),
    ("Tanzania", "Tanzania"),
    ("Tailandia", "Tailandia"),
    ("Timor Oriental", "Timor Oriental"),
    ("Togo", "Togo"),
    ("Tokelau", "Tokelau"),
    ("Tonga", "Tonga"),
    ("Trinidad y Tobago", "Trinidad y Tobago"),
    ("Túnez", "Túnez"),
    ("Turquía", "Turquía"),
    ("Turkmenistan", "Turkmenistan"),
    ("Islas Turcas y Caicos", "Islas Turcas y Caicos"),
    ("Tuvalu", "Tuvalu"),
    ("Uganda", "Uganda"),
    ("Ucrania", "Ucrania"),
    ("Emiratos Árabes Unidos", "Emiratos Árabes Unidos"),
    ("Reino Unido", "Reino Unido"),
    ("Estados Unidos", "Estados Unidos"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistán", "Uzbekistán"),
    ("Vanuatu", "Vanuatu"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Islas Vírgenes Británicas", "Islas Vírgenes Británicas"),
    ("Islas Vírgenes Americanas", "Islas Vírgenes Americanas"),
    ("Sáhara Occidental", "Sáhara Occidental"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),
)


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
    pais = models.CharField(max_length=100, blank=True, choices=paises)
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

