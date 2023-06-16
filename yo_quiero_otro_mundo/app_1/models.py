from django.db import models

# Create your models here.


class Servicios_contratados (models.Model):
    servicio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    mensaje = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Perfil_Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100, unique=True, default='usuario')
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    imagen_perfil = models.ImageField(
        upload_to='static/img/perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario
