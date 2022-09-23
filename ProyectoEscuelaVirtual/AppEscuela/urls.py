from django.urls import path
from AppEscuela.views import inicio, usuarios_, profesores_, cursos_, formulario1, formulario2, formulario3, buscarCursos, buscarProfesores, buscarUsuarios, buscar

# Enlaces de la AppEscuela

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('usuarios', usuarios_, name = 'Usuarios'),
    path('profesores', profesores_, name = 'Profesores'),
    path('cursos', cursos_, name = 'Cursos'),
    path('form1', formulario1, name = 'Formulario1'),
    path('form2', formulario2, name = 'Formulario2'),
    path('form3', formulario3, name = 'Formulario3'),
    path('buscarUsuarios', buscarUsuarios, name = 'BuscarUsuarios'),
    path('buscarProfesores', buscarProfesores, name = 'BuscarProfesores'),
    path('buscarCursos', buscarCursos, name = 'BuscarCursos'),
    path('buscar/', buscar, name = 'Buscar')
]