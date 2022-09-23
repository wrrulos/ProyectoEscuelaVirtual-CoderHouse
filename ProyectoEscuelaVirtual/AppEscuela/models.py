from django.db import models

# Create your models here.

class Usuarios(models.Model):
    """
    Aca se almacenan los datos de los usuarios registrados en la pagina.
    """

    username = models.CharField(max_length=60)  # Nombre de usuario
    nombre = models.CharField(max_length=60)  # Nombres
    apellido = models.CharField(max_length=60)  # Apellidos
    correo = models.CharField(max_length=60)  # Correo electronico
    edad = models.IntegerField()  # Edad
    registro = models.DateTimeField()  # Fecha de registro


class Profesores(models.Model):
    """
    Aca se almacenan los datos de los profesores de la escuela.
    """

    nombre = models.CharField(max_length=60)  # Nombres
    apellido = models.CharField(max_length=60)  # Apellidos
    correo = models.CharField(max_length=60)  # Correo electronico


class Cursos(models.Model):
    """
    Aca se almacenan la lista de cursos disponibles. (Incluye fecha de inicio y fin)
    """

    nombre = models.CharField(max_length=60)  # Nombre del curso
    inicio = models.DateTimeField()  # Fecha del inicio del curso
    fin = models.DateTimeField()  # Fecha del fin del curso
