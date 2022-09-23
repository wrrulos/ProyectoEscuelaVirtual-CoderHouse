from django.contrib import admin
from AppEscuela.models import Usuarios, Profesores, Cursos

admin.site.register(Usuarios)  # Registra el modelo 'Usuarios'
admin.site.register(Profesores)  # Registra el modelo 'Profesores'
admin.site.register(Cursos)  # Registra el modelo 'Cursos'