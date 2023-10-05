from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'admins', views.AdminViewSet)


urlpatterns = [
    path("general", views.general),
    path("usuarios", views.usuarios),
    path("entregas", views.entregas),
    path("opcion", views.opcion),
]
