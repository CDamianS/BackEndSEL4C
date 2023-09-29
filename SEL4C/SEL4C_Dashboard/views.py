from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import loads, dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import requests

# Create your views here.

#funciones



#endpoints
def index(request):
    return HttpResponse("Dashboard")

