from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # Para mostrar mensajes al usuario

# ... tu vista index existente ...
def index(request):
    return HttpResponse("<h1>¡Hola, Django desde Docker!</h1>")

# --- NUEVA VISTA PARA REGISTRO ---
def registro_usuario(request):
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo usuario en la base de datos
            form.save()
            # Obtiene el nombre de usuario para el mensaje
            username = form.cleaned_data.get('username')
            # Añade un mensaje de éxito (opcional)
            messages.success(request, f'¡Cuenta creada exitosamente para {username}!')
            # Redirige a otra página (ej. la página de inicio o login)
            # Asegúrate de tener una URL llamada 'index' o cambia a donde quieras redirigir
            return redirect('index')
        else:
            # Si el formulario no es válido, se mostrarán los errores en la plantilla
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        # Si es una petición GET, crea un formulario vacío
        form = UserCreationForm()

    # Renderiza la plantilla con el formulario
    # Asegúrate de crear la plantilla 'app/registro.html'
    return render(request, 'app/registro.html', {'form': form})
# ---------------------------------

# Puedes tener otras vistas aquí también...