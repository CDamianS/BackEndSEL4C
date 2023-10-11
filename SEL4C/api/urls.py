# API URL configuration.
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"admins", views.AdminViewSet)
router.register(r"actividades", views.ActividadViewSet)
router.register(r"cuestionario_inicial", views.CuestionarioIViewSet)
router.register(r"cuestionario_final", views.CuestionarioFViewSet)
router.register(r"cambio_nombre", views.CambioNViewSet)
router.register(r"cambio_contrasenia", views.CambioCViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),

    path("existe_usuario", views.existe_usuario, name="existe_usuario"),
    path("cuestionario_inicial", views.cuestionario_inicial, name="cuestionario_inicial"),
    path("cuestionario_PC", views.cuestionario_PC, name="cuestionario_PC"),
    path("upload", views.upload, name="upload"),
    path("download/<int:file_id>", views.download, name="download"),

    path("repuestas_cuestionarioI", views.repuestas_cuestionarioI, name='repuestas_cuestionarioI'),
    path("repuestas_cuestionarioF", views.repuestas_cuestionarioF, name='repuestas_cuestionarioF'),

    path("enviar_solicitudN", views.enviar_solicitudN, name="enviar_solicitudN"),
    path("enviar_solicitudC", views.enviar_solicitudC, name="enviar_solicitudC"),

    path("ver_admins", views.ver_admins, name="ver_admins"),
    path("admin/<int:pk>/actualizar", views.actulizar_admins, name="actulizar_admins"),
    path("admin/<int:adminID>/borrar", views.borrar_admins, name="borrar_admins"),
    path("crear_Admin", views.crear_Admin, name="crear_Admin"),

    path("ver_usuarios", views.ver_usuarios, name="ver_usuarios"),
    path("usuario/<int:pk>/ver", views.ver_usuario, name="ver_usuario"),
    path("usuario/<int:pk>/actualizar", views.actualizar_usuario, name="actualizar_usuario"),
    path("usuario/<int:usuarioID>/borrar", views.borrar_usuarios, name="borrar_usuarios"),
    path("crear_Usuario", views.crear_Usuario, name="crear_Usuario"),

    path("ver_actividades", views.ver_actividades, name="ver_actividades"),

    path("ver_ecnuestasI", views.ver_ecnuestasI, name="ver_ecnuestasI"),
    path("ver_ecnuestasF", views.ver_ecnuestasF, name="ver_ecnuestasF"),
    
    path("ver_solicitudes_nombres", views.ver_solicitudes_nombres, name="ver_solicitudes_nombres"),
    path("solicitudN/<int:usuarioID_id>/<str:nombre>/<int:solicitudNID>/cambiar", views.cambiar_nombre,name="cambiar_nombre"),
    
    path("ver_solicitudes_contrasenia", views.ver_solicitudes_contrasenia, name="ver_solicitudes_contrasenia"),
    path("solicitudC/<int:usuarioID_id>/<str:contrasenia>/<int:solicitudCID>/cambiar", views.cambiar_contrasenia, name="cambiar_contrasenia"),
    
]
