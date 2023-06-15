<center>

# Sprint Individual - Módulo 6
### Leonardo Rodenas Escobar

</center>

---
<center>

## **"Yo quiero Otro Mundo"**
``
</center>

La presente entrega comprende el Sprint Final individual del módulo 6, el cual corresponde al conjunto de Aprendizajes esperados del módulo en un sólo proyecto individual. 

La página es una aplicación web desarrollada en Django que simula ser un sitio de difusión de conocimientos sobre agricultura orgánica, reciclaje, cursos y charlas enfocadas a el manejo óptimo de los recursos naturales, agricultura orgánica-biodinámica y cuidado del medio ambiente. 

De esta manera, se muestra a través del sitio noticias en un "carrusel Bootstrap"(por ahora las noticias son sólo una maqueta y serán desarrolladas en entregas posteriores), leer la sección "Nosotros" para conocer un poco más de la empresa, la posibilidad de ver los Servicios entregados en la página, leer recomendaciones de usuarios, ver el equipo detrás de la empresa, contactarse con "Yo quiero Otro Mundo" a través de un fomulario de contacto, la posibilidad de registrarse en el sitio, iniciar sesión y ver una página personalizada (sólo iniciando sesión) donde se pueden ver los cursos y charlas contratados y armar un equipo de trabajo para las mismas.

[![img_1.gif](https://s11.gifyu.com/images/SQLln.gif)](https://gifyu.com/image/SQLln)

---

## Funcionalidades

- **Interfaz intuitiva y fácil de usar:** Interfaz sencilla, minimalista y con el contenido justo para no sobresaturar ni entorpecer el uso de la aplicación. Destacan colores verdes a través del sitio para mantener la uniformidad.
- **Navbar dinámica:** Navbar que cambia su contenido dependiendo de si el usuario tiene su sesión iniciada o no.
- **Revisar redes sociales del sitio:** Tanto la barra superior, como el Footer ofrecen enlaces a las prinicipales redes sociales del sitio.
  
![Animation_Browser4](https://i.imgur.com/KCO0Xen.gif)

- **Despliegue de templates estáticos:** Secciones como "Home, "Nosotros", "Nuestro Equipo" y "Nos Recomiendan" despliegan contenido estático (imágenes). La intención de estos templates es poder contrastarlo con otras partes del sitio que desplegaran contenido dinámico.

[![img_2.gif](https://s12.gifyu.com/images/SQLuL.gif)](https://gifyu.com/image/SQLuL)

- **Registro de Usuarios:** Sólo visible si el usuario no a iniciado sesión, de lo contrario la categoría desaparece de la Navbar. La posibilidad de registrarse en el sitio solicita parámetros obligatorios comunes (nombre , apellido, usuario, correo y contraseña) y la selección a través de un ```<select>``` de un grupo de usuario y auto asignarse permisos. Todos los usuarios registrados son almacenados en la base de datos, de manera que queden disponibles para que un "superadmin" pueda corroborar si necesita o merece los permisos seleccionados o no. Luego del registro, el nuevo usuario es redireccionado al sitio de Login para usar su nueva cuenta registrada. (**Advertencia: reconozco el riesgo que conlleva hacer que un usuario se de permisos a sí mismo, por lo que en un sitio real, fuera de un entorno de aprendizaje no es recomendable, Sin embargo, en la presente entrega esto fue realizado por dos motivos: 1. Aprender a asignar permisos de forma dinámica sin la página de administración de Django y 2. Por que el pdf que describe el trabajo a realizar así lo solicita**)

![Animation_Browser6](https://i.imgur.com/D6OTsjn.gif)

- **Inicio y Cierre de sesión de usuarios:** Si el registro es exitoso, el usuario puede acceder a una página exclusiva (de otro modo inaccesible) con un saludo personalizado con su nombre de usuario, los cursos contratados (inaccesibles por ahora, a futuro serán desarrollados), la posibilidad de armar grupos y un reloj para ver la hora (widget que por ahora sirve sólo como demostración). Si se intenta entrar a esta página sin iniciar sesión, ocurre una redirección automática que redirige al usuario a la página de login. La opción de iniciar sesión actualiza la barra de navegación, de modo que mientras la sesión está en uso, sólo aparece la opción de Logout (cerrar sesión) en vez de la opción de Login (iniciar sesión). 

<center>

![Animation_Browser7](https://i.imgur.com/8wOcwgp.gif)

![Animation_Browser9](https://i.imgur.com/gNP4SwZ.gif)
**Redireccionado automático al intentar entrar al sitio "perfil_usuario.html"sin sesión iniciada**

</center>

- **Armar grupo de trabajo:** Contenido dinámico en el sitio, la página de acceso tras el login (exclusiva para usuarios con una sesión iniciada) permite armar un grupo de trabajo vía web rellenando un formulario con los datos de la persona con la que va a trabajar (esto emula la formación de un grupo de trabajo en caso de tener cursos o charlas contratadas). Los datos ingresados son desplegados en la tarjeta lateral una vez ingresados.

![Animation_Browser8](https://i.imgur.com/NmEHtx6.gif)

- **Vista de los últimos servicios contratados:** Contenido dinámico, permite Visualización de los últimos servicios registrados sin necesidad de utilizar el panel de control provisto por Django admin.


![Animation_Browser10](https://i.imgur.com/IZquEBA.gif)


- **Formulario de contacto dinámico:** Fomulario de contacto que permite dejar un mensaje en la base de datos, para realizar el posterior contacto con el usuario y solucionar las dudas planteadas. Los campos del formulario pasan por verificaciones internas que determinan el largo mínimo y máximo de los mensajes y la obligatoriedad de llenar todos los campos solicitados. En la imagen inferior, en un inicio se llena el mensaje con la palabra "hola", pero el formulario no es válido e indica que el mensaje mínimo debe contener 50 caracteres, tras solucionar esto y escribir un mensaje más largo el formulario es válido y es enviado, avisando de esto en un cuadro inferior de color verde.

[![SQLgz.gif](https://s11.gifyu.com/images/SQLgz.gif)](https://gifyu.com/image/SQLgz)

- **Acceso al panel de Administación de Django:** Acceso y control desde el panel de administración de Django sólo para personal categorizado como Staff y SuperUser. Acá se pueden aplicar los permisos solicitados por lo usuarios registrados y permitirles (o no), entrar al sitio de administración. Los permisos explicados más adelante, restringen funcionalidades a los usuarios y determinan que puede ver y hacer en el proyecto.

![1](https://i.imgur.com/hfQOMwg.png)

---
### Grupos de permisos de Usuario:

Los grupos estan pensado de menor cantidad de permisos (más restringido el uso del sitio) a mayor cantidad (menos restricciones, posee más control del sitio). Ninguno de ellos, a excepción del "superuser" puede entrar al sitio de administración de Django a no ser que el "superuser" les confiera el tipo de usuario Staff o SuperUser.

![1](https://i.imgur.com/PTNmUfJ.png)

- **Visitante:** Solo puede ver las tablas "Formulario_contactos" y "Perfil_Usuarios", todo lo demás está restringido (Emula a alguien que visita la página y aún no está interesado en crear una cuenta).
- **Alumno:** Este grupo tiene los mismos permisos que el grupo anterior, más permisos adicionales como ver, agregar y modificar la tabla "Servicios _contratadoss" (emula a un alumno que tiene cursos o charlas contratadas y que desea modificar la información en sus cursos).
- **Profesor:** El Profesor por su parte tiene todos los permisos de los grupos anteriores y muchos permisos mas, entre los que se incluyen modificar los datos del alumno (cambiarlo de curso) y ver los usuarios registrados, entre otros (como el nombre sugiere emula a un profesor que imparte un curso o charla en la aplicación). Al momento de una usuario registrarse y solicitar permisos de Profesor, el super Admin puede darle permisos de Staff y por tanto ingreso al sitio de Administarción con sus permisos restringidos.
- **Administrador:** Rango máximo tipo de usuario, posee todos los permisos y accesos , ya que posee el estado de "superusuario". Es capaz de controlar a los demás usuarios, entregando o quitando
 permisos y cambiando su tipo de usuario.

---

### Requisitos del sistema

- Python 3.11.3
- Django 4.2.1
- DBeaver (o cualquier otro cliente de base de datos que maneje sqlite)
- Navegador web de su preferencia.
- Conexión estable de internet
- dependencias necesarias para la aplicación se encuentran en archivo requirements.txt

---

### Instrucciones de instalación

1. Clona el repositorio de la aplicación desde GitHub:

```
   git clone https://github.com/Leonardo-Rodenas/Sprint_Individual_6
```

<br>

2. Accede al directorio del proyecto:

<br>

3. Crea un entorno virtual e instala las dependencias desde requeriments.txt :

```Python
   python -m venv (nombre de tu entorno virtual)
   .(nombre de tu entorno virtual)\scripts\activate.bat   
   pip install -r requirements.txt
```

<br>

4. Configura la base de datos:
   
<br>
   - Crea una base de datos en PostgreSQL y actualiza la configuración en el archivo `settings.py`.
   - Si deseas puedes utilzar la base datos por defecto (sqlite3) que trae la aplicación.
  
<br>

5. Aplica las migraciones:
   
``` Python
   python manage.py makemigrations
   python manage.py migrate
```

<br>

6. Inicia el servidor local:

``` Python
   python manage.py runserver
```

<br>

7. Abre tu navegador web y visita **http://localhost:8000** para acceder a la aplicación.

---

### Contribuciones

¡Se agradecen las contribuciones a "Yo quiero Otro Mundo"! Si deseas colaborar, sigue estos pasos:

1. Crea un fork del repositorio
2. Crea una rama para tu nueva función o corrección de error: `git checkout -b nombre-rama`
3. Realiza tus modificaciones y asegúrate de escribir pruebas adecuadas.
4. Realiza un commit de tus cambios: `git commit -m "Descripción de los cambios"`
5. Envía tus cambios al repositorio remoto: `git push origin nombre-rama`
6. Abre una solicitud de extracción en GitHub para que revisemos tus cambios.

---

### Soporte

Si
 tienes alguna pregunta, problema o sugerencia, no dudes en contactarme a través de la sección de "Issues" en GitHub o enviando un correo electrónico a yo_quiero_otro_mundo@gmail.com

¡Gracias por utilizar "Yo_quiero_otro_mundo"!
