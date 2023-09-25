from rest_framework import serializers
from SEL4C_Dashboard.models import (
    Usuario,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
