from django import forms


class FormularioUsuario(forms.Form):
    """
    Formulario que guarda los datos ingresados por el usuario
    """

    username = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    correo = forms.CharField()