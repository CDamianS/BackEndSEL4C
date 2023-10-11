from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'admins', views.AdminViewSet)


urlpatterns = [
    path("", views.general),
    path("general", views.general, name="general"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("entregas", views.entregas, name="entregas"),
    path("cambios", views.cambios, name="cambios"),
    path("usuario/<int:usuario_id>/", views.usuarioGraph, name="usuarioGraph"),
]
