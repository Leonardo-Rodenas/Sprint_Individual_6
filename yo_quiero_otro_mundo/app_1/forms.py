from django import forms

from app_1.models import Perfil_Usuario


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                               max_length=50, min_length=2,
                               error_messages={
                                   'required': 'El usuario es obligatorio',
                                   'max_length': 'El usuario no puede superar los 50 caracteres',
                                   'min_length': 'El usuario debe tener al menos 2 caracteres'
                               },
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Ingrese su usuario',
                                   'class': 'form-control'
                               })
                               )
    password = forms.CharField(label='Contraseña', required=True,
                               max_length=50, min_length=1,
                               error_messages={
                                   'required': 'La contraseña es obligatoria',
                                   'max_length': 'La contraseña no puede superar los 50 caracteres',
                                   'min_length': 'La contraseña debe tener al menos 1 caracter'
                               },
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Ingrese su contraseña',
                                   'class': 'form-control'
                               })
                               )


class Formulario_de_Contacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True,
                             max_length=50,
                             error_messages={
                                 'required': 'El nombre es obligatorio',
                                 'max_length': 'El nombre no puede superar los 50 caracteres'
                             },
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Ingrese su nombre',
                                 'class': 'form-control'
                             }),
                             )
    apellido = forms.CharField(label='Apellido', required=True,
                               max_length=50,
                               error_messages={
                                   'required': 'El apellido es obligatorio',
                                   'max_length': 'El apellido no puede superar los 50 caracteres'
                               },
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Ingrese su apellido',
                                   'class': 'form-control'
                               }),
                               )
    ciudad = forms.CharField(label='Ciudad', required=True,
                             max_length=50,
                             error_messages={
                                 'required': 'La ciudad es obligatoria',
                                 'max_length': 'La ciudad no puede superar los 50 caracteres'
                             },
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Ingrese su ciudad',
                                 'class': 'form-control'
                             }),
                             )
    email = forms.EmailField(label='Email', required=True,
                             max_length=150, min_length=6,
                             error_messages={
                                 'required': 'El e-mail es obligatorio',
                                 'max_length': 'El e-mail no puede superar los 150 caracteres',
                                 'min_length': 'El e-mail debe tener al menos 6 caracteres'
                             },
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Ingrese su correo electrónico',
                                 'class': 'form-control'
                             })
                             )
    telefono = forms.CharField(label='Teléfono', required=True,
                               max_length=15, min_length=9,
                               error_messages={
                                   'required': 'El teléfono es obligatorio',
                                   'max_length': 'El teléfono no puede superar los 15 caracteres',
                                   'min_length': 'El teléfono debe tener al menos 9 caracteres'
                               },
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'No olvide tus número de teléfono',
                                   'class': 'form-control'
                               })
                               )
    mensaje = forms.CharField(label='Mensaje', required=True,
                              max_length=1000, min_length=50,
                              error_messages={
                                  'required': 'El mensaje es obligatorio',
                                  'max_length': 'El mensaje no puede superar los 1000 caracteres',
                                  'min_length': 'El mensaje debe tener al menos 50 caracteres'
                              },
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Cuentanos... ¿Cuál es tu motivo de contacto?',
                                  'class': 'form-control'
                              })
                              )


class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Perfil_Usuario
        fields = ('nombre', 'apellido', 'nombre_usuario',
                  'correo', 'telefono', 'imagen_perfil')
        widget = {
            'class': 'my-3'
        }
