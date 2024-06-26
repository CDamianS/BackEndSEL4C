from rest_framework import serializers
from .models import Admin, Usuario, Actividad, CuestionarioInicial, CuestionarioFinal, CambioNombre, CambioContrasenia

class AdminSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'
    
class CuestionarioISerializer(serializers.ModelSerializer):
    class Meta:
        model = CuestionarioInicial
        fields = '__all__'

class CuestionarioFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuestionarioFinal
        fields = '__all__'

class CambioNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioNombre
        fields = '__all__'

class CambioContraseniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioContrasenia
        fields = '__all__'
