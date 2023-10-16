from django import forms
from .models import Admin, Usuario, Actividad, CuestionarioInicial, CuestionarioFinal, CambioNombre, CambioContrasenia

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['nombre', 'contrasenia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'contrasenia': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contrasenia', 'email', 'avance', 'genero', 'edad', 'pais', 'institucion', 'grado', 'diciplina', 'respuestasI']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'contrasenia': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'email': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'avance': forms.NumberInput(attrs={'class': 'contenedor-input-entrada'}),
            'edad': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'pais': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'institucion': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'grado': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
            'diciplina': forms.TextInput(attrs={'class': 'contenedor-input-entrada'}),
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'estatus', 'usuarioID', 'entregable']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class CuestionarioIForm(forms.ModelForm):
    class Meta:
        model = CuestionarioInicial
        fields = ['numero', 'respuesta', 'usuarioID']  

class CuestionarioFForm(forms.ModelForm):
    class Meta:
        model = CuestionarioFinal
        fields = ['numero', 'respuesta', 'usuarioID']       

class CambioNForm(forms.ModelForm):
    class Meta:
        model = CambioNombre
        fields = ['nombre', 'usuarioID', 'estatus']

class CambioCForm(forms.ModelForm):
    class Meta:
        model = CambioContrasenia
        fields = ['contrasenia', 'usuarioID', 'estatus']