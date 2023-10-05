# API URL configuration.
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from api import views
from .views import *

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
<<<<<<< Updated upstream
=======
router.register(r"admins", views.AdminViewSet)
router.register(r"cuestionario_inicial", views.CuestionarioIViewSet)
router.register(r"cuestionario_final", views.CuestionarioFViewSet)
>>>>>>> Stashed changes

urlpatterns = [
    path("", include(router.urls)),
    path("existe_usuario", views.existe_usuario, name='existe_usuario'),
<<<<<<< Updated upstream
    path("cuestionario_inicial", cuestionario_inicial),
    path('user_login', views.user_login, name='user_login')
=======
    path('user_login', views.user_login, name='user_login'),
    path("cuestionario_inicial", views.cuestionario_inicial, name='cuestionario_inicial'),
    path("cuestionario_PC", views.cuestionario_PC, name='cuestionario_PC'),
    path("upload", views.upload, name='upload'),
    path("download/<int:file_id>", views.download, name='download'),
    path("creacion_usuario", views.creacion_usuario, name='creacion_usuario'),
    path("mandar_respuestas", views.mandar_respuestas, name='mandar_respuestas'),

    path("ver_admins", views.ver_admins, name='ver_admins'),
    path("admin/<int:pk>/actualizar", views.actulizar_admins, name='actulizar_admins'),
    path("admin/<int:adminID>/borrar", views.borrar_admins, name='borrar_admins'),

    path("ver_usuarios", views.ver_usuarios, name='ver_usuarios'),
    path("usuario/<int:pk>/actualizar", views.actualizar_usuario, name='actualizar_usuario'),
>>>>>>> Stashed changes
]
