from django.urls import path
from . import views
from .views import Formulario_Contacto, IngresoView, combina_lista_usuarios_y_registro, lista_servicios_contratados, equipo, perfil_usuario, recomiendan, info_sobre_nosotros
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', lista_servicios_contratados, name='lista_servicios'),
    path('equipo/', equipo, name='equipo'),
    path('recomiendan/', recomiendan, name='recomiendan'),
    path('sobre_nosotros/', info_sobre_nosotros, name='sobre_nosotros'),
    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
    path('login/', IngresoView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contacto/', Formulario_Contacto.as_view(), name='contacto'),
    path('info_perfil/', combina_lista_usuarios_y_registro, name='info_perfil'),  
]
