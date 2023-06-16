from django.contrib import admin
from .models import FormularioContacto, Perfil_Usuario, Servicios_contratados

# Register your models here.

admin.site.register(Servicios_contratados)
admin.site.register(FormularioContacto)
admin.site.register(Perfil_Usuario)