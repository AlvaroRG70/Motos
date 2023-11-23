from django.forms import ModelForm
from moto.models import Moto, Concesionario
from datetime import date




class MotoForm(ModelForm):
    class Meta:
        model = Moto
        fields = ['nombre', 'marca', 'modelo', 'año', 'precio', 'usuario', 'comentador']
        labels = {
            "nombre": ("Nombre de la moto"),
            "marca": ("marca"),
            "modelo": ("modelo"),
            "año": ("año de la moto"),
            "precio": ("precio"),
            "usuario": ("usuario"),
            "comentador": ("comentador")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "modelo": ("50 caracteres como máximo"),
        }
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        marca = self.cleaned_data.get("marca")
        modelo = self.cleaned_data.get("modelo")
        año = self.cleaned_data.get("año")
        precio = self.cleaned_data.get("precio")
        usuario = self.cleaned_data.get("usuario")
        comentador = self.cleaned_data.get("comentador")
        
        #comprobamos que no existan 2 motos con el mismo nombre
        '''
        motoNombre = Moto.objects.filter(nombre=nombre).first()
        if (not motoNombre is None):
            self.add_error("nombre", "Ya existe una moto con ese nombre")
        '''        
    
        if len(nombre) < 3 :
            self.add_error("nombre", "Debe tener al menos 3 caracteres")
            
        #que al menos se pueda seleccionar una marca
          
        if len(marca) < 1:
            self.add_error("marca", "Debe seleccionar una marca")
            
        #que el modelo tenga minimo 3 caracteres
        
        if len(modelo) < 3:
            self.add_error("modelo", "Debe seleccionar tener 3 caracteres")
        
        #año tiene que ser menor que el actual o igual
        
        fechaHoy = date.today()
        if año > fechaHoy.year:
            self.add_error("año", "Debe ser igual o menor al año actual")
            
        #precio no puede ser negativo
        
        if precio <= 0:
            self.add_error("precio", "Debe ser mayor que 0")
            
        #tiene que seleccionar al menos 1 usuario
        
        if len(usuario) < 1:
            self.add_error("precio", "Debe seleccionar al menos 1 usuario")
            
        #tiene que seleccionar 2 comentadores
        
        if len(comentador) < 1:
            self.add_error("precio", "Debe seleccionar al menos 1 comentador")
            
        return self.cleaned_data
    
  
class ConcesionarioForm(ModelForm):
    class Meta:
        model = Concesionario
        fields = ['nombre', 'ubicacion', 'telefono', 'fecha_apertura', 'descripcion', 'moto']
        labels = {
            "nombre": ("Nombre de la moto"),
            "ubicacion": ("Ubicacion"),
            "telefono": ("Introduzca el teléfono"),
            "fecha_apertura": ("fecha de apertura"),
            "descripcion": ("Descripcion"),
            "moto": ("Moto")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "telefono": ("9 caracteres"),
        }
    

        
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        ubicacion = self.cleaned_data.get("ubicacion")
        telefono = self.cleaned_data.get("telefono")
        fecha_apertura = self.cleaned_data.get("fecha_apertura")
        descripcion = self.cleaned_data.get("descripcion")
        moto = self.cleaned_data.get("moto")
        
        #comprobamos que no existan 2 motos con el mismo nombre
    
        
        
        
        
        
        
        
        
        
        


