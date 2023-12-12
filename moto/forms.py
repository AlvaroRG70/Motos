from django import forms
from django.forms import ModelForm
from moto.models import Moto, Concesionario, Boutique, Evento
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
    
  

        
        #comprobamos que no existan 2 motos con el mismo nombre
    
        
        
        
class MotoBusquedaForm(forms.Form):
    textoBusqueda = forms.CharField(required=True)
        
class BusquedaAvanzadaMotoForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)
    marca = forms.MultipleChoiceField(choices=Moto.MARCA,
                                required=False,
                                widget=forms.CheckboxSelectMultiple()
                               )
    anyo = forms.IntegerField(required=False)
    precio = forms.IntegerField(required=False)

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        marca=self.cleaned_data.get('marca')
        anyo=self.cleaned_data.get('anyo')
        precio=self.cleaned_data.get('precio')

        if(textoBusqueda == ""
           and len(marca) == 0
           and precio is None
           and anyo is None):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('marca','Debes introducir algún valor')
            self.add_error('anyo','Debes introducir algún valor')
            self.add_error('precio','Debes introducir algún valor')
            
        else:
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')

        return self.cleaned_data    
    



    
    
    
    
#CRUD concesionario

    
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
    
#CRUD ARTÍCULOS
    
#CREAR
class ArticuloForm(ModelForm):
    class Meta:
        model = Boutique
        fields = ['nombre', 'tipo', 'descripcion', 'precio', 'talla', 'stock']
        labels = {
            "nombre": ("Nombre del artículo"),
            "tipo": ("tipo"),
            "descripcion": ("descripcion"),
            "precio": ("precio"),
            "talla": ("talla"),
            "stock": ("stock")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "modelo": ("50 caracteres como máximo"),
        }
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        tipo = self.cleaned_data.get("tipo")
        descripcion = self.cleaned_data.get("descripcion")
        precio = self.cleaned_data.get("precio")
        talla = self.cleaned_data.get("talla")
        stock = self.cleaned_data.get("stock")
        
        
        if len(nombre) < 4:
            self.add_error("nombre", "Debe tener al menos 4 caracteres")
            
        if len(tipo) < 4:
            self.add_error("tipo", "Debe tener al menos 4 caracteres")
        
        if len(descripcion) < 10:
            self.add_error("descripcion", "Debe contener 10 caracteres como mínimo")
            
        if precio < 0:
            self.add_error("precio", "Debe ser positivo")
        
        if len(talla) < 1:
            self.add_error("talla", "Debe seleccionar una talla")
        
        if stock < 0:
            self.add_error("stock", "Debe ser positivo")    
        
        
        return self.cleaned_data
    
    

#crud eventos

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'hora', 'ubicacion', 'descripcion', 'usuario']
        labels = {
            "nombre": ("Nombre del artículo"),
            "fecha": ("fecha"),
            "hora": ("hora"),
            "ubicacion": ("ubicacion"),
            "descripcion": ("descripcion"),
            "usuario": ("usuario")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "usuario": ("50 caracteres como máximo"),
        }
        
        widgets = {
            "fecha":forms.SelectDateWidget()
        }
        localized_fields = ["fecha"]
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        fecha = self.cleaned_data.get("fecha")
        hora = self.cleaned_data.get("hora")
        ubicacion = self.cleaned_data.get("ubicacion")
        descripcion = self.cleaned_data.get("descripcion")
        usuario = self.cleaned_data.get("usuario")
        
        
        if len(nombre) < 4:
            self.add_error("nombre", "Debe tener al menos 4 caracteres")
            
        fechaHoy = date.today()
        if fecha > fechaHoy:
            self.add_error("fecha", "Debe ser igual o menor a la fecha actual")
            
        if len(ubicacion) < 4:
            self.add_error("ubicacion", "Debe tener al menos 4 caracteres")
        
        if len(descripcion) < 10:
            self.add_error("descripcion", "Debe contener 10 caracteres como mínimo")
        
        if len(usuario) < 1:
            self.add_error("usuario", "Debe elegir al menos 1")
    
        
        
        return self.cleaned_data
        
        
class BusquedaAvanzadaEventoForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')

        if(textoBusqueda == ""):
            self.add_error('textoBusqueda','Debes introducir algún valor')

        return self.cleaned_data
