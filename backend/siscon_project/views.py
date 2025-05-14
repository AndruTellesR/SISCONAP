from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bienvenido al Sistema de Gestión Presupuestal SISCON</h1>
        <p>Utiliza el menú para navegar por las funcionalidades.</p>
    """)
