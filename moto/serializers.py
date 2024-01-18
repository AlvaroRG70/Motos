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

        
    
    
    