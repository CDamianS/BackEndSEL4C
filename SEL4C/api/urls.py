# API URL configuration.
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from api import views
from .views import *

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("existe_usuario", views.existe_usuario, name='existe_usuario'),
    path("cuestionario_inicial", cuestionario_inicial),
    path('user_login', views.user_login, name='user_login')
]
