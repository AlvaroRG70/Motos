from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *
from django.db.models import Q,Prefetch, Avg,Max,Min, F

@api_view(['GET'])
def moto_list(request):
    
    motos = Moto.objects.all()
    serializer = UsuarioSeializerMejorado(motos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def concesionario_list(request):
    
    conc = Concesionario.objects.all()
    serializer = ConcesionarioSeializerMejorado(conc, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def evento_list(request):
    
    eventos = Evento.objects.all()
    serializer = EventoSeializerMejorado(eventos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def moto_buscar_api(request):
    
        formulario = MotoBusquedaForm(request.query_params)
        
        if formulario.is_valid():
            texto = formulario.cleaned_data.get('textoBusqueda')
            motos = Moto.objects.prefetch_related("usuario")
            motos = motos.filter(Q(nombre__contains=texto) | Q(modelo__contains=texto)).all()
            serializer = UsuarioSeializerMejorado(motos, many=True)
            return Response(serializer.data)
        else:
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
