from django.urls import include, path
from rest_framework import routers
from . import views
from api import urls

router = routers.DefaultRouter()
#router.register(r'admins', views.AdminViewSet)


urlpatterns = []