from django.shortcuts import render
from django.http import JsonResponse
from .models import Rubro

# Create your views here.

def rubro_list_api(request):
    """
    API view to list all Rubro objects.
    """
    if request.method == 'GET':
        rubros = Rubro.objects.all()
        data = [{"id": rubro.id, "codigo": rubro.codigo, "nombre": rubro.nombre, "monto_inicial": str(rubro.monto_inicial)} for rubro in rubros]
        return JsonResponse(data, safe=False, status=200)
    else:
        return JsonResponse({"error": "Se requiere una solicitud GET."}, status=400)
