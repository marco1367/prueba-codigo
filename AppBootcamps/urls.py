from django.urls import path
from AppBootcamps.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cursos', cursos, name="Cursos"),
    path('entregables', entregables, name="Entregables"),
    path('estudiantes', estudiantes, name="Estudiantes"),
    path('profesores', profesores, name="Profesores"),
    path('buscarCamada-formulario', BuscarFormulario, name="BuscarCamada-formulario"),
    path('buscar', Buscar),
    path('leerProfesores', leerProfesores, name="leerProfesores"),
    path('eliminar-profesor/<profesor_nombre>', EliminarProfesor, name="EliminarProfesor"),
    path('editar-profesor/<profesor_nombre>', editarProfesores, name="EditarProfesor"),
    ##----Vistas basadas en clases-----##
    path('cursos-list', CursoList.as_view(), name='CursosList')
    ##---------------------------------##
]