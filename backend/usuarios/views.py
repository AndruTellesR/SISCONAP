from django.shortcuts import render
from django.contrib.auth.models import User # Importar el modelo User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# Vista para listar todos los usuarios
# @login_required # Descomentar si solo usuarios logueados pueden ver esto
# @permission_required('auth.view_user', raise_exception=True) # Descomentar para requerir permiso específico
def listar_usuarios(request):
    """
    Obtiene todos los usuarios y los muestra en una plantilla.
    """
    lista_usuarios = User.objects.all().order_by('username') # Obtener todos los usuarios ordenados
    
    # Decidir qué plantilla usar. Podríamos crear una nueva o adaptar una existente.
    # Por ahora, supongamos que adaptaremos 'other/sample-page.html'
    # O mejor, creemos una específica: 'usuarios/lista_usuarios.html'
    # template_name = 'usuarios/lista_usuarios.html' # Asumiremos que crearemos este archivo luego
    template_name = 'other/sample-page.html' # Usar la plantilla sample-page existente

    context = {
        'usuarios': lista_usuarios,
        'page_title': 'Gestión de Usuarios', # Título para la plantilla
        # Puedes añadir más contexto si tu plantilla base lo necesita
    }
    return render(request, template_name, context)

# Aquí podríamos añadir más vistas (crear usuario, editar, eliminar) luego.
