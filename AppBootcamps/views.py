import email
from django.http import HttpResponse
from django.shortcuts import render
from AppBootcamps.models import *
from AppBootcamps.forms import *

from django.views.generic import ListView


class CursoList(ListView):
    model: Curso
    template_name: "cursos_list.html"


# Create your views here.
def inicio(request):
    return render(request, "AppBootcamps/inicio.html")



def cursos(request):
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Curso(nombre=info['nombre'], camada=info['camada'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppBootcamps/cursos.html", {"miFormulario": miFormulario})




def entregables(request):
    if request.method == "POST":
        
        miFormulario = EntregablesFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Entregable(nombre=info['nombre'], fechaDeEntrega=info['fechaDeEntrega'], entregado=info['entregado'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = EntregablesFormulario()
    return render(request, "AppBootcamps/entregables.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/entregables.html")




def estudiantes(request):
    if request.method == "POST":
        
        miFormulario = EstudiantesFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = EstudiantesFormulario()
    return render(request, "AppBootcamps/estudiantes.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/estudiantes.html")




def profesores(request):
    if request.method == "POST":
        
        miFormulario = ProfesoresFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            curso = Profesor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])
            curso.save()
            return render(request, "AppBootcamps/inicio.html")
    else:
        miFormulario = ProfesoresFormulario()
    return render(request, "AppBootcamps/profesores.html", {"miFormulario": miFormulario})
    # return render(request, "AppBootcamps/profesores.html")



def BuscarFormulario(request):
    return render(request, "AppBootcamps/buscarFormulario.html")

def Buscar(request):
    # respuesta = f"Estoy buscando la camada n°: {request.GET['camada']}"

    # return HttpResponse(respuesta)
    
    if request.GET['camada']:
        camada_a_buscar = request.GET['camada']
        cursos_encontrados = Curso.objects.filter(camada=camada_a_buscar)

        return render(request, "AppBootcamps/busquedaResultado.html", {"cursos": cursos_encontrados, "camada": camada_a_buscar})
    else:
        respuesta = "No enviaste datos para buscar"
        return render(request, "AppBootcamps/busquedaResultado.html", {"respuesta": respuesta})


def leerProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores

    context = {"profesores": profesores}

    return render(request, "AppBootcamps/leerProfesores.html", context)


def EliminarProfesor(request, profesor_nombre):

    ##Buscamos el/los proferos/res con el nombre {prefesor_nombre}
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    ##Volvemos a traer todos los profesores:
    profesores = Profesor.objects.all() #trae todos los profesores y redirigimos al mismo template (es como actualizar)
    context = {"profesores": profesores}
    return render(request, "AppBootcamps/leerProfesores.html", context)



def editarProfesores(request, profesor_nombre):
    #Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    print('profesor---->', profesor)

    #Si es POST hago lo mismo que el agregar un profesor:
    if request.method == 'POST':
        
        miFormulario = ProfesoresFormulario(request.POST)

        if miFormulario.is_valid() :
            data = miFormulario.cleaned_data

            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.profesion = data['profesion']

            profesor.save()

            return render(request, "AppBootcamps/inicio.html")

    else:
        miFormulario = ProfesoresFormulario(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion
        })
    
    #Voy al html que me permite editar:
    return render(request, "AppBootcamps/editarProfesor.html", {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})
