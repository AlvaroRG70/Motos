from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .forms import *
from django.db.models import Q,Prefetch, Avg,Max,Min,F
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    
    
#busqueda avanzada 
@api_view(['GET'])
def moto_buscar_avanzado_api(request):
    
        if (len(request.query_params)>0):
            formulario = BusquedaAvanzadaMotoForm(request.GET)
            if formulario.is_valid():
                mensaje="Se ha buscado por:\n"
                
                QSmotos = Moto.objects.prefetch_related("usuario")
                
                textoBusqueda=formulario.cleaned_data.get('textoBusqueda')
                marca = formulario.cleaned_data.get('marca')
                anyo = formulario.cleaned_data.get('anyo')
                precio = formulario.cleaned_data.get('precio')

                if textoBusqueda is not None:
                    QSmotos = QSmotos.filter(Q(nombre__contains=textoBusqueda) | Q(marca__contains=textoBusqueda) | Q(modelo__contains=textoBusqueda))
                    mensaje+=" Contiene: "+ textoBusqueda+"\n"
                
                if(len(marca)>0):
                    mensaje +=" la marca sea "+marca[0]
                    filtroOR = Q(marca=marca[0])
                    for marca in marca[1:]:
                        mensaje += " o "+marca[1]
                        filtroOR |= Q(marca=marca)
                    mensaje += "\n"
                    QSmotos =  QSmotos.filter(filtroOR)
                
                if anyo is not None:
                    QSmotos = QSmotos.filter(año__startswith=anyo)
                    mensaje+= str(anyo)+"\n"
                    
                if precio is not None:
                    QSmotos = QSmotos.filter(precio__startswith=precio)
                    mensaje+= str(precio)+"\n"
                    
                
                motos = QSmotos.all()
                serializer = UsuarioSeializerMejorado(motos, many=True)
                
                return Response(serializer.data)
            else:
                return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)