from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'admins', views.AdminViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('',views.index, name='index'), 
    path('admin_auth', views.admin_auth, name='admin_auth'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('crar_Admin', views.crar_Admin, name='crar_Admin'),

]