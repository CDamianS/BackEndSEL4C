# API URL configuration.
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('cuestionario_inicial', cuestionario_inicial),
    # path('validar_usario', login_required(set_play_ended), name='set_play_ended'),
    # path('register_usuario', login_required(add_student_to_game), name='add_student_to_game'),
]
