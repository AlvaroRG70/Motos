from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .forms import *
from django.db.models import Q,Prefetch, Avg,Max,Min,F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView



class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def moto_list(request):
    motos = Moto.objects.all()
    serializer = MotoSerializerMejorado(motos, many=True)
    data = serializer.data

    # Agregar la URL de la imagen a cada moto en la respuesta
    for moto_data in data:
        moto = Moto.objects.get(id=moto_data['id'])
        moto_data['imagen_url'] = moto.imagen.url if moto.imagen else None

    return Response(data)


@api_view(['GET'])
def motos_filtradas_por_caballos(request):

    # 0- Descendete
    # 1- Ascendente
    # if( orden == 0):
    #      motos_filtradas = Moto.objects.order_by('-caballos')
    # else:
    #      motos_filtradas = Moto.objects.order_by('caballos')
    
    motos_filtradas = Moto.objects.order_by('-caballos')
    serializer = MotoSerializerMejorado(motos_filtradas, many=True)
    data = serializer.data
    for moto_data in data:
        moto = Moto.objects.get(id=moto_data['id'])
        moto_data['imagen_url'] = moto.imagen.url if moto.imagen else None

    return Response(data)

from django.db.models import Count
from django.http import JsonResponse
from datetime import datetime

@api_view(['GET'])
def reservas_list(request):
    
    reservas = MotosReservada.objects.all()
    serializer = MotosReservadaSerializer(reservas  , many=True)
    print(serializer.data)
    return Response(serializer.data)
    
@api_view(['POST'])
def reserva_create(request):  
    if(request.user.has_perm("moto.add_valoracion")):
    
        serializers = ReservaSerializerCreate(data=request.data)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Reserva AÑADIDA")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['POST'])
# def informe_motos_reservadas(request):
#     if request.method == 'POST':
#         # Obtener el mes y año actual
#         fecha_actual = datetime.now()
#         mes_actual = fecha_actual.month
#         año_actual = fecha_actual.year

#         # Filtrar las motos reservadas del mes actual
#         motos_reservadas = MotosReservada.objects.filter(fecha__month=mes_actual, fecha__year=año_actual)

#         # Contar la cantidad de reservas para cada moto
#         reservas_por_moto = motos_reservadas.values('moto__nombre').annotate(reservas=Count('moto'))

#         # Preparar los datos para la respuesta
#         informe = {
#             'mes': mes_actual,
#             'año': año_actual,
#             'motos_reservadas': [
#                 {'nombre': reserva['moto__nombre'], 'reservas': reserva['reservas']} 
#                 for reserva in reservas_por_moto
#             ]
#         }

#         return JsonResponse(informe)
#     else:
#         return JsonResponse({'error': 'Método HTTP no admitido'}, status=405)

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
def valoracion_list(request):
    
    valoraciones = Valoracion.objects.all()
    serializer = ValoracionSerializer(valoraciones, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def concesionario_list(request):    
    
    conc = Concesionario.objects.all()
    serializer = ConcesionarioSeializerMejorado(conc, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def moto_buscar_api(request):
    
        formulario = MotoBusquedaForm(request.query_params)
        
        if formulario.is_valid():
            texto = formulario.cleaned_data.get('textoBusqueda')
            motos = Moto.objects.prefetch_related("usuario")
            motos = motos.filter(Q(nombre__contains=texto) | Q(modelo__contains=texto)).all()
            serializer = MotoSerializerMejorado(motos, many=True)
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
                serializer = MotoSerializerMejorado(motos, many=True)
                
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
    if(request.user.has_perm("moto.add_concesionario")):
        serializers = MotoSerializerCreate(data=request.data)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Moto CREADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)
        


@api_view(['GET']) 
def moto_obtener(request,moto_id):
   
    moto = Moto.objects.prefetch_related("usuario")
    moto = moto.get(id=moto_id)
    serializer = MotoSerializerMejorado(moto)
    return Response(serializer.data)

        

@api_view(['PUT'])
def moto_editar(request,moto_id):
    if(request.user.has_perm("moto.change_moto")):
        moto = Moto.objects.get(id=moto_id)
        serializers = MotoSerializerMejorado(data=request.data,instance=moto)
        if serializers.is_valid():
            try:    
                serializers.save()
                return Response("Moto EDITADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['PATCH'])
def moto_actualizar_nombre(request,moto_id):
    if(request.user.has_perm("moto.change_moto")):
    
        serializers = MotoSerializerCreate(data=request.data)
        moto = Moto.objects.get(id=moto_id)
        serializers = MotoSerializerActualizarNombre(data=request.data,instance=moto)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Moto EDITADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['DELETE'])
def moto_eliminar(request,moto_id):
    if(request.user.has_perm("moto.delete_moto")):

        moto = Moto.objects.get(id=moto_id)
        try:
            moto.delete()
            return Response("Moto ELIMINADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def valoracion_create(request):  
    if(request.user.has_perm("moto.add_valoracion")):
    
        serializers = ValoracionSerializerCreate(data=request.data)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("valoracion CREADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def concesionario_create(request):  
    if(request.user.has_perm("moto.add_concesionario")):
    
        serializers = ConcesionarioSerializerCreate(data=request.data)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Concesionario CREADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET']) 
def concesionario_obtener(request,concesionario_id):
    concesionario = Concesionario.objects.all()
    concesionario = concesionario.get(id=concesionario_id)
    serializer = ConcesionarioSeializerMejorado(concesionario)
    return Response(serializer.data)
    
    
@api_view(['PUT'])
def concesionario_editar(request,concesionario_id):
    if(request.user.has_perm("moto.change_concesionario")):

        concesionario = Concesionario.objects.get(id=concesionario_id)
        serializers = ConcesionarioSeializerMejorado(data=request.data,instance=concesionario)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Concesionario EDITADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PATCH'])
def concesionario_actualizar_nombre(request,concesionario_id):
    if(request.user.has_perm("moto.change_concesionario")):
    
        serializers = ConcesionarioSerializerCreate(data=request.data)
        concesionario = Concesionario.objects.get(id=concesionario_id)
        serializers = ConcesionarioSerializerActualizarNombre(data=request.data,instance=concesionario)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Concesionario EDITADO")
            except Exception as error:
                print("Error 500:"+repr(error))
                return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)  

    

@api_view(['DELETE'])
def concesionario_eliminar(request,concesionario_id):
    if(request.user.has_perm("moto.delete_concesionario")):
    
        concesionario = Concesionario.objects.get(id=concesionario_id)
        try:
            concesionario.delete()
            return Response("Concesionario ELIMINADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED) 
    
    
@api_view(['GET']) 
def evento_obtener(request,evento_id):
    evento = Evento.objects.all()
    evento = evento.get(id=evento_id)
    serializer = EventoSeializerMejorado(evento)
    return Response(serializer.data)


@api_view(['POST'])
def evento_create(request):  
    if(request.user.has_perm("moto.add_evento")):
    
        serializers = EventoSerializerCreate(data=request.data)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Evento CREADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def evento_editar(request,evento_id):
    if(request.user.has_perm("moto.change_evento")):
    
        evento = Evento.objects.get(id=evento_id)
        serializers = EventoSeializerMejorado(data=request.data,instance=evento)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("evento EDITADO")
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(['PATCH'])
def evento_actualizar_nombre(request,evento_id):
    if(request.user.has_perm("moto.change_evento")):
    
        serializers = EventoSerializerCreate(data=request.data)
        evento = Evento.objects.get(id=evento_id)
        serializers = EventoSerializerActualizarNombre(data=request.data,instance=evento)
        if serializers.is_valid():
            try:
                serializers.save()
                return Response("Evento EDITADO")
            except Exception as error:
                print("Error 500:"+repr(error))
                return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)   

    
@api_view(['DELETE'])
def evento_eliminar(request,evento_id):
    if(request.user.has_perm("moto.delete_evento")):
    
        evento = Evento.objects.get(id=evento_id)
        try:
            evento.delete()
            return Response("Evento ELIMINADO")
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response("No tiene permisos", status=status.HTTP_401_UNAUTHORIZED)   
    
    
from rest_framework import generics
from rest_framework.permissions import AllowAny

class registrar_usuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializerRegistro
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializers = UsuarioSerializerRegistro(data=request.data)
        if serializers.is_valid():
            try:
                rol = int(request.data.get('rol'))
                user = UsuarioLogin.objects.create_user(
                        username = serializers.data.get("username"), 
                        email = serializers.data.get("email"), 
                        password = serializers.data.get("password1"),
                        rol = rol,
                        )
                if(rol == UsuarioLogin.CLIENTE):
                    grupo = Group.objects.get(name='Clientes') 
                    grupo.user_set.add(user)
                    clientes = cliente.objects.create( usuario = user)
                    clientes.save()
                elif(rol == UsuarioLogin.TRABAJADOR):
                    grupo = Group.objects.get(name='Trabajadores') 
                    grupo.user_set.add(user)    
                    trabajadores = TrabajadorLogin.objects.create(usuario = user)
                    trabajadores.save()
                usuarioSerializado = UsuarioLoginSeria(user)
                return Response(usuarioSerializado.data)
            except Exception as error:
                print(repr(error))
                return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





from oauth2_provider.models import AccessToken     
@api_view(['GET'])
def obtener_usuario_token(request,token):
    ModeloToken = AccessToken.objects.get(token=token)
    usuario = UsuarioLogin.objects.get(id=ModeloToken.user_id)
    serializer = UsuarioLoginSeria(usuario)
    return Response(serializer.data)
    

    