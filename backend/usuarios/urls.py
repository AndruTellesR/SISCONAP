# backend/usuarios/urls.py
from django.urls import path
from . import views # Importar las vistas de la app actual

app_name = 'usuarios' # Namespace para las URLs de esta app

urlpatterns = [
    path('', views.listar_usuarios, name='lista_usuarios'),
    # Aquí añadiremos más rutas para crear, editar, etc. luego
]
