from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from repositorio.models import *
from .forms import * 


# Create your views here.
def home (request):
    return render (request, "repositorio/index.html")

def alumno (request):
    contexto = {"alumnos": Alumno.objects.all()}
    return render (request, "repositorio/alumno.html", contexto)

def profesor (request):
    contexto = {"profesor": Profesor.objects.all()}
    return render (request, "repositorio/profesor.html", contexto)

def materia (request):
    contexto = {"materias": Materia.objects.all()}
    return render (request, "repositorio/materia.html", contexto)

def mundoliterario (request):
    return render (request, "repositorio/MundoLiterario.html")

def acerca (request):
    return render (request, "repositorio/acerca.html")

# Formularios

def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'repositorio/alumno_form.html', {'form': form})

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'repositorio/alumno_list.html', {'alumnos': alumnos})

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'repositorio/profesor_form.html', {'form': form})

def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'repositorio/profesor_list.html', {'profesores': profesores})

def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'repositorio/materia_form.html', {'form': form})

def materia_list(request):
    materia = Profesor.objects.all()
    return render(request, 'repositorio/materia_list.html', {'profesores': materia})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'repositorio/curso_form.html', {'form': form})