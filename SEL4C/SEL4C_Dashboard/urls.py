from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'admins', views.AdminViewSet)


urlpatterns = [
    path("", views.general, name="general"),
    path("general", views.general, name="general"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("entregas", views.entregas, name="entregas"),
    path("cambios", views.cambios, name="cambios"),
    path("administradores", views.administradores, name="administradores"),
    path("usuario/<int:usuario_id>/", views.usuarioGraph, name="usuarioGraph"),
    path(
        "usuario/<int:usuarioID>/borrar", views.borrar_usuarios, name="borrar_usuarios"
    ),
    path("admin/<int:adminID>/borrar", views.borrar_admins, name="borrar_admins"),
]
