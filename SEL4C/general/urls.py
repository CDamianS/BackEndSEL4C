from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("descargar_app", views.descargar_app, name="descargar_app"),
    path("existe_admin", views.existe_admin, name="existe_admin"),
    path("admin_login", views.admin_login, name="admin_login"),
]