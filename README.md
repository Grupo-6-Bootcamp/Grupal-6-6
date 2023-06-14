# Grupal-6-5 - Grupo 5 Alvaro Manterola - Cynthia Abarca - Esteban Santibañez - Guido Saavedra

# Funcionalidades

1. Página sencilla en la que se muestran las funcionalidades de Django para limitar el acceso a páginas privadas ('homeprivado') con el decorador "@method_decorator(login_required, name='dispatch')"

2. También cuenta con un login/logout y página privada, a la cual el usuario es redireccionado una vez que las credenciales son correctas.

Con esta sección verificamos el usuario y su contraseña. De estar todo correcto, es redireccionado a 'homeprivado':

        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('homeprivado')

Por consiguiente tenemos una condicional en la que las credenciales sean incorrectas el usuario vería una alerta de error con el mensaje "Usuario no encontrado"

        else:
            context = {"error": "Usuario no encontrado",
                       'formulario_login': FormularioLogin()}
            return render(request, 'login.html', context)


En caso de que el usuario desee cerrar sesión utilizamos la siguiente sección de código el cual redirecciona al usuario luego de utilizar un input en cerrar sesión

        class CerrarSesion(View):
            def get(self, request):
                logout(request)
                return redirect('index')

3. Finalmente comentamos un poquito sobre ('homeprivado')

    Luego de la sentencia if usuario not None
    if usuario is not None:
            login(request, usuario)
            return redirect('homeprivado')
Nos vamos a encontrar con un index minimalista el cual mostrará un título dándole saber al usuario que ingreso a la página, en conjunto con un saludo personalizado

# Levantar aplicación.

Django nos facilita nuestro proceso de levantar la app en '4' simples pasos tendremos la aplicación en funcionamiento

1. Creamos un entorno virtual con un nombre a nuestra elección python -m venv nombre_venv
2. Activamos el mismo
    En windows: source Script\activate.bat
    En Unix/MacOS: tutorial-env/bin/activate
3. Instalamos los paquetes necesarios, estos van incluidos en nuestra app por lo que solamente ejecutaremos el siguiente comando:
    pip install -r requirements.txt
4. Con nuestro entorno activado y todos los paquetes instalados correctamente ingresamos a la recta final

# INPUT:

        python manage.py makemigrations

        python manage.py migrate

        python manage.py runserver [PUERTO] / (8000 POR DEFECTO)  

# OUTPUT

        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        June 08, 2023 - 12:39:31
        Django version 4.2.1, using settings 'telovendo.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

5. Si el output es como en el punto anterior en nuestro browser ingresamos a 127.0.0.1:[PUERTO] o (CTRL + CLICK http://127.0.0.1:8000/)
Y ya tendríamos la aplicación corriendo en un servidor local para trabajar en ella.

# Credenciales para ingresar como super usuario
Usuario: admin
Contraseña: admin

# Usuario de prueba
User: testuser
Password letmeinfortest# Grupal-6-6
