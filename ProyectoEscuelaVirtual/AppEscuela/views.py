from django.shortcuts import render
from django.http import HttpResponse
from AppEscuela.models import Usuarios, Profesores, Cursos
from AppEscuela.forms import FormularioUsuario
from datetime import datetime


def inicio(request):
    return render(request, 'AppEscuela/inicio.html')


def usuarios_(request):
    return render(request, 'AppEscuela/usuarios.html')


def profesores_(request):
    return render(request, 'AppEscuela/profesores.html')


def cursos_(request):
    return render(request, 'AppEscuela/cursos.html')


def formulario1(request):
    """
    Formulario que guarda los datos de los usuarios.
    """

    if request.method == 'POST':  # SI el usuario le da clic al boton.
        formulario = FormularioUsuario(request.POST)

        if formulario.is_valid():  # Comprueba si no hay errores con el formulario.
            info = formulario.cleaned_data  # Guarda los datos del formulario en la variable 'info'
            usuario = Usuarios(username = info['username'], nombre = info['nombre'], apellido = info['apellido'], correo = info['correo'], edad = info['edad'], registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            usuario.save()  # Guarda los datos en la base de datos
            
            return render(request, 'AppEscuela/inicio.html')

    else:
        formulario = FormularioUsuario()  # Muestra el formulario vacío


    return render(request, 'AppEscuela/form1.html', {'form':formulario})


def buscarUsuarios(request):
    return render(request, 'AppEscuela/buscarUsuarios.html')

def buscarProfesores(request):
    return render(request, 'AppEscuela/buscarUsuarios.html')

def buscarCursos(request):
    return render(request, 'AppEscuela/buscarUsuarios.html')

def buscar(request):
    if request.GET["correo_usuarios"]:  # Si la petición es username
        resultados = Usuarios.objects.filter(correo__icontains = request.GET["correo_usuarios"])
        return render(request, 'AppEscuela/resultados.html', {"tipo_de_busqueda": "correo_usuarios", 'resultados':resultados, 'busqueda':request.GET["correo_usuarios"]})

    elif request.GET["correo_usuarios"]:  # Si la petición es username
        resultados = Usuarios.objects.filter(correo__icontains = request.GET["correo_profesor"])
        return render(request, 'AppEscuela/resultados.html', {"tipo_de_busqueda": "correo_profesor", 'resultados':resultados, 'busqueda':request.GET["correo_profesor"]})

    else:
        mensaje = 'Es necesario especificar un dato.'

    return HttpResponse(mensaje)




def guardarCurso(request):
    """
    Guarda un curso
    """

    curso = Cursos(nombre = 'Ciberseguridad', inicio = '2022-09-23 16:00:00', fin = '2022-10-24 00:00:00')
    curso.save()

    return HttpResponse('Guardado')