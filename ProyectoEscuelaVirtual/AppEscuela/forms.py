from django import forms


class FormularioUsuario(forms.Form):
    """
    Formulario que guarda los datos ingresados por el usuario a la db de Usuarios
    """

    username = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    correo = forms.CharField()


class FormularioProfesor(forms.Form):
    """
    Formulario que guarda los datos ingresados por el usuario a la db de Profesores
    """

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.CharField()


class FormularioCurso(forms.Form):
    """
    Formulario que guarda los datos ingresados por el usuario a la db de Cursos
    """

    nombre = forms.CharField()
    inicio = forms.DateTimeField()
    fin = forms.DateTimeField()