# API URL configuration.
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"admins", views.AdminViewSet)
router.register(r"cuestionario_inicial", views.CuestionarioIViewSet)
router.register(r"cuestionario_final", views.CuestionarioFViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('',views.index, name='index'), 
    path('descargar_app', views.descargar_app, name='descargar_app'),
    #path('<path:not_found>', views.error_404, name='error_404'),
    path('existe_admin', views.existe_admin, name='existe_admin'),
    path('admin_login', views.admin_login, name='admin_login'),
    
    path("existe_usuario", views.existe_usuario, name='existe_usuario'),
    path('user_login', views.user_login, name='user_login'),
    path("cuestionario_inicial", views.cuestionario_inicial, name='cuestionario_inicial'),
    path("cuestionario_PC", views.cuestionario_PC, name='cuestionario_PC'),
    path("upload", views.upload, name='upload'),
    path("download/<int:file_id>", views.download, name='download'),
    #path("creacion_usuario", views.creacion_usuario, name='creacion_usuario'),
    path("repuestas_cuestionario", views.repuestas_cuestionario, name='repuestas_cuestionario'),

    path("ver_admins", views.ver_admins, name='ver_admins'),
    path("admin/<int:pk>/actualizar", views.actulizar_admins, name='actulizar_admins'),
    path("admin/<int:adminID>/borrar", views.borrar_admins, name='borrar_admins'),
    path('crear_Admin', views.crear_Admin, name='crear_Admin'),

    path("ver_usuarios", views.ver_usuarios, name='ver_usuarios'),
    path("usuario/<int:pk>/actualizar", views.actualizar_usuario, name='actualizar_usuario'),
    path("usuario/<int:usuarioID>/borrar", views.borrar_usuarios, name='borrar_usuarios'),
    path("crear_Usuario", views.crear_Usuario, name='crear_Usuario'),

    path("ver_actividades", views.ver_actividades, name='ver_actividades'),

    path("ver_ecnuestasI", views.ver_ecnuestasI, name='ver_ecnuestasI'),
    path("ver_ecnuestasF", views.ver_ecnuestasF, name='ver_ecnuestasF'),
]
