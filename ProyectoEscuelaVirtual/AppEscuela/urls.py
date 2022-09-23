from django.urls import path
from AppEscuela.views import buscarUsuarios, inicio, usuarios_, profesores_, cursos_, formulario1, buscar

# Enlaces de la AppEscuela

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('usuarios', usuarios_, name = 'Usuarios'),
    path('profesores', profesores_, name = 'Profesores'),
    path('cursos', cursos_, name = 'Cursos'),
    path('form1', formulario1, name = 'Formulario1'),
    path('buscarUsuarios', buscarUsuarios, name = 'BuscarUsuarios'),
    path('buscar/', buscar, name = 'Buscar')
]