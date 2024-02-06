from rest_framework import serializers
from .models import *
from datetime import date


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
        fields = ('id','nombre', 'marca', 'modelo', 'año', 'precio', 'usuario')




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
    
    def validate_año(self,año):
        if año > 2024:
             raise serializers.ValidationError('tiene que ser menos al año actual')
        return año
    
    def validate_descripcion(self,descripcion):
        if len(descripcion) < 10:
             raise serializers.ValidationError('Al menos debes indicar 10 caracteres')
        return descripcion
    
    
    def validate_usuario(self,usuario):
        if len(usuario) < 1:
            raise serializers.ValidationError('Debe seleccionar al menos un usuario')
        return usuario


class ConcesionarioSerializerCreate(serializers.ModelSerializer):
 
    class Meta:
        model = Concesionario
        fields = ['nombre','ubicacion','telefono',
                  'fecha_apertura','descripcion','moto']
    
    def validate_nombre(self,nombre):
        ConcesionarioNombre = Concesionario.objects.filter(nombre=nombre).first()
        if(not ConcesionarioNombre is None
           ):
             if(not self.instance is None and ConcesionarioNombre.id == self.instance.id):
                 pass
             else:
                raise serializers.ValidationError('Ya existe un concesionario con ese nombre')
        
        return nombre
    
    def validate_ubicacion(self,ubicacion):
        if len(ubicacion) < 10:
             raise serializers.ValidationError('Al menos debes indicar 10 caracteres')
        return ubicacion
    
    def validate_telefono(self,telefono):
        if len(str(telefono)) != 9:
             raise serializers.ValidationError('debes indicar 9 caracteres')
        return telefono
    
    #def validar_fecha_apertura(self, fecha_apertura):
     #   fechaHoy = date.today()
      #  if fecha_apertura >= fechaHoy:
       #     raise serializers.ValidationError('La fecha de apertura debe ser anterior a la fecha actual.')
        #return fecha_apertura

    def validate_descripcion(self,descripcion):
        if len(descripcion) < 10:
             raise serializers.ValidationError('Al menos debes indicar 10 caracteres')
        return descripcion
    
    
    def validate_moto(self,moto):
        if len(moto) < 1:
            raise serializers.ValidationError('Debe seleccionar al menos un moto')
        return moto

    
    
    