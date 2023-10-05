from django.contrib import admin
from .models import Admin, Usuario, Actividad, CuestionarioInicial, CuestionarioFinal

# Register your models here.
default_app_config = 'my_app.apps.MyAppConfig'
admin.site.register(Admin)
admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(CuestionarioInicial)
admin.site.register(CuestionarioFinal)