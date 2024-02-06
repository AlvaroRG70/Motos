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
#@permission_classes([IsAuthenticated])
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
def usuario_list(request):
    
    usuarios = Usuario.objects.all()
    serializer = UsuarioRealSerializer(usuarios, many=True)
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
        

@api_view(['GET'])
def concesionario_busqueda_avanzada_api(request):

    if (len(request.query_params)>0):
        formulario = BusquedaAvanzadaConcesionarioForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSconcesionario = Concesionario.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')
            telefono=formulario.cleaned_data.get('telefono')

            if textoBusqueda is not None:
                QSconcesionario = QSconcesionario.filter(Q(nombre__contains=textoBusqueda) | Q(ubicacion__contains=textoBusqueda) | Q(descripcion__contains=textoBusqueda))
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            if telefono is not None:
                QSconcesionario = QSconcesionario.filter(telefono__startswith=telefono)
                mensaje+= str(telefono)+"\n"
            
            concesionario = QSconcesionario.all()
            
            serializer = ConcesionarioSeializerMejorado(concesionario, many=True)
            
            return Response(serializer.data)
        else:
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
#eventos

@api_view(['GET'])
def evento_busqueda_avanzada_api(request):

    if (len(request.query_params)>0):
        formulario = BusquedaAvanzadaEventoForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSevento = Evento.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')

            if textoBusqueda is not None:
                QSevento = QSevento.filter(Q(nombre__contains=textoBusqueda) | Q(descripcion__contains=textoBusqueda)| Q(ubicacion__contains=textoBusqueda) )
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            evento = QSevento.all()
            
            serializer = EventoSeializerMejorado(evento, many=True)
            
            return Response(serializer.data)
        else:
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
    
# motos

@api_view(['POST'])
def moto_create(request):  
    serializers = MotoSerializerCreate(data=request.data)
    if serializers.is_valid():
        try:
            serializers.save()
            return Response("Moto CREADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET']) 
def moto_obtener(request,moto_id):
    moto = Moto.objects.prefetch_related("usuario")
    moto = moto.get(id=moto_id)
    serializer = UsuarioSeializerMejorado(moto)
    return Response(serializer.data)

@api_view(['PUT'])
def moto_editar(request,moto_id):
    print(Response.json())
    moto = Moto.objects.get(id=moto_id)
    serializers = UsuarioSeializerMejorado(data=request.data,instance=moto)
    if serializers.is_valid():
        try:
            serializers.save()
            return Response("Moto EDITADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def concesionario_create(request):  
    serializers = ConcesionarioSerializerCreate(data=request.data)
    if serializers.is_valid():
        try:
            serializers.save()
            return Response("Concesionario CREADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)