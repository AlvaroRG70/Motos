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
        
        
#create

class MotoSerializerCreate(serializers.ModelSerializer):
 
    class Meta:
        model = Moto
        fields = ['nombre','marca','modelo',
                  'año','precio','usuario']
    
    def validate_nombre(self,nombre):
        MotoNombre = Moto.objects.filter(nombre=nombre).first()
        if(not MotoNombre is None
           ):
             if(not self.instance is None and MotoNombre.id == self.instance.id):
                 pass
             else:
                raise serializers.ValidationError('Ya existe una moto con ese nombre')
        
        return nombre
    
    def validate_descripcion(self,año):
        if año > 2024:
             raise serializers.ValidationError('tiene que ser menos al año actual')
        return descripcion
    
    def validate_anyo(self,descripcion):
        if len(descripcion) < 10:
             raise serializers.ValidationError('Al menos debes indicar 10 caracteres')
        return descripcion
    
    
    def validate_usuario(self,usuario):
        if len(usuario) < 1:
            raise serializers.ValidationError('Debe seleccionar al menos un usuario')
        return usuario


    
    
    