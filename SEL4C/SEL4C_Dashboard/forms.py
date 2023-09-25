from django import forms
from .models import Admin, Usuario, Actividad, CuestionarioInicial, CuestionarioFinal

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['nombre', 'contrasenia']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contrasenia', 'email', 'avance', 'genero', 'edad', 'pais', 'institucion', 'grado', 'diciplina']

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'estatus', 'usuarioID', 'entregable']

class CuestionarioIForm(forms.ModelForm):
    class Meta:
        model = CuestionarioInicial
        fields = ['pregunta', 'respuesta', 'usuarioID']   

class CuestionarioFForm(forms.ModelForm):
    class Meta:
        model = CuestionarioFinal
        fields = ['pregunta', 'respuesta', 'usuarioID']       