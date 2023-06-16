from typing import Any, Dict
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistroUsuarioForm
from .models import Perfil_Usuario, Servicios_contratados
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from app_1.forms import Formulario_de_Contacto
from app_1.models import FormularioContacto

# Create your views here.

def home(request):
    return render(request, 'index.html')

def lista_servicios_contratados(request):
    servicios = Servicios_contratados.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def equipo(request):
    return render(request, 'equipo.html')

def recomiendan(request):
    return render(request, 'recomiendan.html')

def info_sobre_nosotros(request):
    return render(request, 'nosotros.html')

@login_required
def perfil_usuario(request):
    return render(request, 'perfil_usuario.html')

class IngresoView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('perfil_usuario')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"form": form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

class Formulario_Contacto (TemplateView):
  template_name = 'templates_app/contacto.html'
  
  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context["info"] = "Información complementaria"
    return context

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    context["formulario"] = Formulario_de_Contacto()
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    form = Formulario_de_Contacto(request.POST)
    mensajes = {
      "enviado": False,
      "resultado": None
    }
    if form.is_valid():
      nombre = form.cleaned_data['nombre']
      apellido = form.cleaned_data['apellido']
      ciudad = form.cleaned_data['ciudad']
      telefono = form.cleaned_data['telefono']
      email = form.cleaned_data['email']
      mensaje = form.cleaned_data['mensaje']

      registro = FormularioContacto(
        nombre=nombre,
        apellido=apellido,
        ciudad=ciudad,
        telefono=telefono,
        email=email,
        mensaje=mensaje
      )
      registro.save()

      mensajes = { "enviado": True, "resultado": "Mensaje enviado correctamente" }
    else:
      mensajes = { "enviado": False, "resultado": form.errors }
    return render(request, self.template_name, { "formulario": form, "mensajes": mensajes})

@login_required
def combina_lista_usuarios_y_registro(request):
    usuarios_query = Perfil_Usuario.objects.values()  # Obtiene los valores del QuerySet
    usuarios = list(usuarios_query)  # Convierte el QuerySet en una lista de diccionarios
    form = RegistroUsuarioForm(request.POST, request.FILES)
    contexto_combinado = {'usuarios': usuarios, 'form': form}
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('info_perfil')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'info_perfil.html', contexto_combinado)