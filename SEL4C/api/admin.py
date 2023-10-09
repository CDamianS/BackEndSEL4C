from django.contrib import admin
from .models import Admin, Usuario, Actividad, CuestionarioInicial, CuestionarioFinal, CambioNombre, CambioContrasenia

# Register your models here.
default_app_config = 'my_app.apps.MyAppConfig'
admin.site.register(Admin)
admin.site.register(Usuario)
admin.site.register(Actividad)
admin.site.register(CuestionarioInicial)
admin.site.register(CuestionarioFinal)
admin.site.register(CambioNombre)
admin.site.register(CambioContrasenia)