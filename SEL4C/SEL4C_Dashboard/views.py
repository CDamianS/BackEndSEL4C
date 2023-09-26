from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import loads, dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Admin
from .serializers import AdminSerialiizer
from .forms import AdminForm
import requests


# Create your views here.

#funciones
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerialiizer

def validar_admin(name, password):
    try:
        admin = Admin.objects.get(nombre = name, contrasenia = password)
        admin_id = admin.adminID
    except:
        admin_id = None
    return admin_id


#endpoints
def index(request):
    return HttpResponse("Dashboard")

@csrf_exempt
def admin_login(request):
    return render(request, 'admin_login.html')

@csrf_exempt
def admin_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin_id = validar_admin(username, password)
        if admin_id is not None:
            return HttpResponse("Logeado!!")
        else:
            return HttpResponse("No existes como usuario :(")
        

@csrf_exempt
def crear_Admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ok!!!")
        else:
            
            error_message = form.errors.values()
            for error in error_message:
                print(error)
            
            return HttpResponse("erorr :(")
    else:
        form = AdminForm()
    return render(request, 'admin_creacion(prueb).html', {'form': form})
