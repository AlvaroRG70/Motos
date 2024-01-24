from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'
        
class UsuarioRealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
class UsuarioSeializerMejorado(serializers.ModelSerializer):
    usuario = UsuarioRealSerializer(read_only=True, many=True)
    marca = serializers.CharField(source='get_marca_display')

    class Meta:
        model = Moto
        fields = ('nombre', 'marca', 'modelo', 'año', 'precio', 'usuario')




#serializer concesionario
class ConcesionarioSeializerMejorado(serializers.ModelSerializer):
    moto = UsuarioSerializer(read_only=True, many=True)
    fecha_apertura = serializers.DateField(format='get_marca_display')

    class Meta:
        model = Concesionario
        fields = ('nombre', 'ubicacion', 'telefono', 'fecha_apertura', 'descripcion', 'moto')
        

#serializer evento
class EventoSeializerMejorado(serializers.ModelSerializer):
    usuario = UsuarioRealSerializer(read_only=True, many=True)
    fecha = serializers.DateField(format='get_marca_display')

    class Meta:
        model = Evento
        fields = ('nombre', 'fecha', 'hora', 'ubicacion', 'descripcion', 'usuario')


    
    
    