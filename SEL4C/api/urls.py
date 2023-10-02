# API URL configuration.
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"admins", views.AdminViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path("", include(router.urls)),
    path('existe_admin', views.existe_admin, name='existe_admin'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('crear_Admin', views.crear_Admin, name='crear_Admin'),
    path("existe_usuario", views.existe_usuario, name='existe_usuario'),
    path('user_login', views.user_login, name='user_login'),
    path("cuestionario_inicial", views.cuestionario_inicial, name='cuestionario_inicial'),
    path("cuestionario_PC", views.cuestionario_PC, name='cuestionario_PC'),
    path("upload", views.upload, name='upload'),
    path("creacion_usuario", views.creacion_usuario, name='creacion_usuario'),
]
