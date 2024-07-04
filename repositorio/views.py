from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from repositorio.models import *

# Create your views here.
def home (request):
    return render (request, "repositorio/index.html")

def alumno (request):
    contexto = {"alumnos": Alumno.objects.all()}
    return render (request, "repositorio/alumno.html", contexto)

def docente (request):
    contexto = {"docentes": Profesor.objects.all()}
    return render (request, "repositorio/docente.html", contexto)

def materia (request):
    return render (request, "repositorio/materia.html")

def mundoliterario (request):
    return render (request, "repositorio/MundoLiterario.html")