from django.shortcuts import render
from django.http import HttpResponse
from AppEscuela.models import Usuarios, Profesores, Cursos
from AppEscuela.forms import FormularioCurso, FormularioUsuario, FormularioProfesor
from datetime import datetime


def inicio(request):
    """
    Muestra la pagina de inicio
    """

    return render(request, 'AppEscuela/inicio.html')


def usuarios_(request):
    """
    Muestra la pagina de administración de usuarios
    """
    return render(request, 'AppEscuela/usuarios.html')


def profesores_(request):
    """
    Muestra la pagina de administración de profesores
    """

    return render(request, 'AppEscuela/profesores.html')


def cursos_(request):
    """
    Muestra la pagina de administración de cursos
    """
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

    return render(request, 'AppEscuela/form.html', {'form':formulario})


def formulario2(request):
    """
    Formulario que guarda los datos de los profesores.
    """

    if request.method == 'POST':  # SI el usuario le da clic al boton.
        formulario = FormularioProfesor(request.POST)

        if formulario.is_valid():  # Comprueba si no hay errores con el formulario.
            info = formulario.cleaned_data  # Guarda los datos del formulario en la variable 'info'
            profesor = Profesores(nombre = info['nombre'], apellido = info['apellido'], correo = info['correo'])
            profesor.save()  # Guarda los datos en la base de datos
            
            return render(request, 'AppEscuela/inicio.html')

    else:
        formulario = FormularioProfesor()  # Muestra el formulario vacío

    return render(request, 'AppEscuela/form.html', {'form':formulario})


def formulario3(request):
    """
    Formulario que guarda los datos de los cursos.
    """

    if request.method == 'POST':  # SI el usuario le da clic al boton.
        formulario = FormularioCurso(request.POST)

        if formulario.is_valid():  # Comprueba si no hay errores con el formulario.
            info = formulario.cleaned_data  # Guarda los datos del formulario en la variable 'info'
            curso = Cursos(nombre = info['nombre'], inicio = info['inicio'], fin = info['fin'])
            curso.save()  # Guarda los datos en la base de datos
            
            return render(request, 'AppEscuela/inicio.html')

    else:
        formulario = FormularioCurso()  # Muestra el formulario vacío

    return render(request, 'AppEscuela/form.html', {'form':formulario})


def buscarUsuarios(request):
    """
    Pagina que busca el correo de los usuarios.
    """

    return render(request, 'AppEscuela/buscarUsuarios.html')

def buscarProfesores(request):
    """
    Pagina que busca el correo de los profesores.
    """

    return render(request, 'AppEscuela/buscarProfesores.html')

def buscarCursos(request):
    """
    Pagina que busca el nombre de los cursos.
    """

    return render(request, 'AppEscuela/buscarCursos.html')


def buscar(request):
    """
    Pagina que busca los datos en la base de datos (correos y nombres de cursos)
    """

    try:
        if request.GET["correo_usuarios"]:  # Si la petición es correo_usuarios
            resultados = Usuarios.objects.filter(correo__icontains = request.GET["correo_usuarios"])
            return render(request, 'AppEscuela/resultados.html', {"tipo_de_busqueda": "correo_usuarios", 'resultados':resultados, 'busqueda':request.GET["correo_usuarios"]})

    except KeyError:
        pass

    try:
        if request.GET["correo_profesor"]:  # Si la petición es correo_profesor
            resultados = Profesores.objects.filter(correo__icontains = request.GET["correo_profesor"])
            return render(request, 'AppEscuela/resultados.html', {"tipo_de_busqueda": "correo_profesor", 'resultados':resultados, 'busqueda':request.GET["correo_profesor"]}) 

    except KeyError:
        pass
    
    try:
        if request.GET["nombre_curso"]:  # Si la petición es nombre_curso
            resultados = Cursos.objects.filter(nombre__icontains = request.GET["nombre_curso"])
            return render(request, 'AppEscuela/resultados.html', {"tipo_de_busqueda": "nombre_curso", 'resultados':resultados, 'busqueda':request.GET["nombre_curso"]})

    except KeyError:
        return HttpResponse('Es necesario especificar un dato.')