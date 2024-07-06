from django.urls import path, include
from repositorio.views import *
 
urlpatterns = [
    path('', home, name="home"),
    path('materia/', materia, name="materia"),
    path('alumno/', alumno, name="alumno"),
    path('docente/', docente, name="docente"),
    path('mundoliteriario/', mundoliterario, name="mundoliterario"),
    path('acerca/', acerca, name="acerca"),
]