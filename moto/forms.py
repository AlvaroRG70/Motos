from django import forms
from django.forms import ModelForm
from moto.models import Moto, Concesionario, Boutique, Evento, Usuario, Trabajador, Promocion, UsuarioLogin, Prestamo
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm



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
            "nombre": ("Nombre"),
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
    
        if len(nombre) < 4:
            self.add_error("nombre", "Debe tener al menos 4 caracteres")
            
        if len(ubicacion) < 10:
            self.add_error("ubicacion", "Debe tener al menos 10 caracteres")
            
            
        if len(descripcion) < 10:
            self.add_error("descripcion", "Debe tener al menos 10 caracteres")
        
        if len(str(telefono)) < 9 and len(str(telefono)) > 9:
            self.add_error("descripcion", "Debe contener 9 caracteres")

        if len(moto) < 1:
            self.add_error("moto", "Debe seleccionar 2 moto")
        
        
      
        
        
        return self.cleaned_data
    

class BusquedaAvanzadaConcesionarioForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)
    telefono = forms.IntegerField(required=False)

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        telefono=self.cleaned_data.get('telefono')

        if(textoBusqueda == ""
           and telefono is None):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('telefono','Debes introducir algún valor')
            
        else:
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')

            if (not telefono is None and len(str(telefono)) != 9):
                self.add_error('telefono','Debe tener 9 digitos')

        return self.cleaned_data
    
    

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
    
    
class BusquedaAvanzadaArticuloForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)
    talla = forms.MultipleChoiceField(choices=Boutique.TALLA,
                                required=False,
                                widget=forms.CheckboxSelectMultiple()
                               )
    stock = forms.IntegerField(required=False)
    precio = forms.IntegerField(required=False)

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        talla=self.cleaned_data.get('talla')
        stock=self.cleaned_data.get('stock')
        precio=self.cleaned_data.get('precio')

        if(textoBusqueda == ""
           and len(talla) == 0
           and precio is None
           and stock is None):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('talla','Debes introducir algún valor')
            self.add_error('precio','Debes introducir algún valor')
            self.add_error('stock','Debes introducir algún valor')
            
        else:
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')
                
            if (not precio is None and precio < 0):
                self.add_error('precio','Debe introducir ser positivo')
                

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
            "fecha":forms.SelectDateWidget(years=range(1950, 2030))
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


#CRUD USUARIOS

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'correo_electronico', 'contraseña', 'fecha_nacimiento', 'fecha_registro', 'preferencias']
        labels = {
            "nombre": ("Nombre del artículo"),
            "apellidos": ("apellidos"),
            "correo_electronico": ("correo_electronico"),
            "contraseña": ("contraseña"),
            "fecha_nacimiento": ("fecha_nacimiento"),
            "fecha_registro": ("fecha_registro"),
            "preferencias": ("preferencias")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "correo_electronico": ("Debe ser un correo válido"),
        }
        
        widgets = {
            "fecha_nacimiento":forms.SelectDateWidget(years=range(1950, 2030)),
            "fecha_registro":forms.SelectDateWidget(years=range(1950, 2030))
        }
        
        localized_fields = ["fecha_nacimiento", "fecha_registro"]
        
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        apellidos = self.cleaned_data.get("apellidos")
        correo_electronico = self.cleaned_data.get("correo_electronico")
        contraseña = self.cleaned_data.get("contraseña")
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        fecha_registro = self.cleaned_data.get("fecha_registro")
        preferencias = self.cleaned_data.get("preferencias")
        
        
        if len(nombre) < 3:
            self.add_error("nombre", "Debe tener al menos 3 caracteres")
        
        if len(apellidos) < 4:
            self.add_error("apellidos", "Debe tener al menos 4 caracteres")
            
        if len(correo_electronico) < 3:
            self.add_error("descripcion", "Debe contener 3 caracteres como mínimo")
            
        fechaHoy1 = date.today()
        if fecha_nacimiento > fechaHoy1:
            self.add_error("fecha_nacimiento", "Debe ser igual o menor a la fecha actual")
        
        fechaHoy2 = date.today()
        if fecha_registro.date() > fechaHoy2:
            self.add_error("fecha_registro", "Debe ser igual o menor a la fecha actual")
        
        
        if len(preferencias) < 10:
            self.add_error("preferencias", "Debe contener 10 caracteres como mínimo")
    
         
        return self.cleaned_data
    
    

class BusquedaAvanzadaUsuarioForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)
    fecha_nacimiento = forms.DateField(label='fecha_nacimiento', widget= forms.SelectDateWidget(years=range(1900,2023))
                                )

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento')

        if(textoBusqueda == ""
           and fecha_nacimiento is None):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('fecha_nacimiento','Debes introducir algún valor')
            
        else:
            
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')
            
            fechaHoy = date.today()
            if not fecha_nacimiento is None and fecha_nacimiento > fechaHoy:
                 self.add_error('fecha_nacimiento','Debe ser menor que la fecha actual')

        return self.cleaned_data
    

#CRUD TRABAJADOR

class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'correo_electronico', 'contraseña', 'fecha_nacimiento', 'concesionario', 'taller']
        labels = {
            "nombre": ("Nombre del artículo"),
            "apellidos": ("apellidos"),
            "correo_electronico": ("correo_electronico"),
            "contraseña": ("contraseña"),
            "fecha_nacimiento": ("fecha_nacimiento"),
            "concesionario": ("concesionario"),
            "taller": ("taller")
        }
        
        help_texts = {
            "nombre": ("50 caracteres como máximo"),
            "apellidos": ("50 caracteres como máximo"),
        }
        
        widgets = {
            "fecha_nacimiento":forms.SelectDateWidget(years=range(1950, 2030))
        }
        localized_fields = ["fecha_nacimiento"]
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        apellidos = self.cleaned_data.get("apellidos")
        correo_electronico = self.cleaned_data.get("correo_electronico")
        contraseña = self.cleaned_data.get("contraseña")
        fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        concesionario = self.cleaned_data.get("concesionario")
        taller = self.cleaned_data.get("taller")
        
        
        if len(nombre) < 3:
            self.add_error("nombre", "Debe tener al menos 3 caracteres")
            
        if len(apellidos) < 3:
            self.add_error("apellidos", "Debe tener al menos 3 caracteres")
            
        if len(correo_electronico) < 5:
            self.add_error("correo_electronico", "Debe tener al menos 5 caracteres")
            
        if len(contraseña) < 7:
            self.add_error("contraseña", "Debe tener al menos 7 caracteres")
            
        fechaHoy = date.today()
        if fecha_nacimiento > fechaHoy:
            self.add_error("fecha_nacimiento", "Debe ser igual o menor a la fecha actual")
            
        
        
        return self.cleaned_data


class BusquedaAvanzadaTrabajadorForm(forms.Form):
    
    textoBusqueda = forms.CharField(required=False)
    fecha_nacimiento = forms.DateField(label='fecha_nacimiento', 
                        widget= forms.SelectDateWidget(years=range(1900,2023))
                        )

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento')
    
        if(textoBusqueda == ""
            and fecha_nacimiento is None):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('fecha_nacimiento','Debes introducir algún valor')
            
        else:
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')
            
            
            fechaHoy = date.today()
            if not fecha_nacimiento is None and fecha_nacimiento > fechaHoy:
                 self.add_error('fecha_nacimiento','Debe ser menor que la fecha actual')
                

        return self.cleaned_data
    
    
    #CRUD EXAMEN
    
    #CREATE
    
class PromocionForm(ModelForm):
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion', 'descuento', 'usuario', 'fecha_fin']
        labels = {
            "nombre": ("Nombre de la promocion"),
            "descripcion": ("Descripción de la promoción"),
            "descuento": ("Descuento que se le aplica"),
            "usuario": ("Usuario al que se le aplica la promoción"),
            "fecha_fin": ("Fecha fin promocion"),
        }
        
        help_texts = {
            "descripcion": ("100 caracteres como mínimo"),
            "nombre": ("el nombre tiene que ser único"),
            "fecha_fin": ("Esta fecha no puede inferior a la fecha actual"),
            "descripcion": ("100 caracteres como mínimo"),
            "descuento": ("valor entre 0 y 100"),
        }
        
        widgets = {
            "fecha_fin":forms.SelectDateWidget(years=range(2023, 2090))
        }
        localized_fields = ["fecha_fin"]
        
        
    def clean(self):
        super().clean()
        nombre = self.cleaned_data.get("nombre")
        descripcion = self.cleaned_data.get("descripcion")
        descuento = self.cleaned_data.get("descuento")
        usuario = self.cleaned_data.get("usuario")
        fecha_fin = self.cleaned_data.get("fecha_fin")
        
        promocionNombre = Promocion.objects.filter(nombre=nombre).first()
        try:
            if(not promocionNombre is None):
                self.add_error('nombre','Ya existe una promocion con ese nombre')
        except ObjectDoesNotExist:
            pass
        
        
        if len(descripcion) < 100:
            self.add_error("descripcion", "Debe contener 100 caracteres como mínimo")
        
        if descuento < 0 or descuento > 100 :
            self.add_error("descuento", "Debe comprender un rango entre 0 y 100") 
               
        fechaHoy = date.today()
        if fecha_fin < fechaHoy:
            self.add_error("fecha_fin", "Debe ser mayor a la fecha actual")
        
        return self.cleaned_data
    
    
#BUSQUEDA

class BusquedaAvanzadaPromocionForm(forms.Form):
    textoBusqueda = forms.CharField(required=False)
    descuento = forms.IntegerField(required=False)
    fecha_desde = forms.DateField(label="fecha_desde",
                                required=False,
                                widget= forms.SelectDateWidget(years=range(2023,209))
                                )
    
    fecha_hasta = forms.DateField(label="fecha_hasta",
                                  required=False,
                                  widget= forms.SelectDateWidget(years=range(2023,209))
                                  )

  

    def clean(self):
        super().clean()
        textoBusqueda=self.cleaned_data.get('textoBusqueda')
        descuento= self.cleaned_data.get('descuento')
        fecha_desde = self.cleaned_data.get('fecha_desde')
        fecha_hasta = self.cleaned_data.get('fecha_hasta')
        usuarios = self.cleaned_data.get('usuarios')
        

        if(textoBusqueda == ""
           and fecha_desde is None
           and fecha_hasta is None
           and descuento is None
           and len(usuarios) == 0
           ):
            
            self.add_error('textoBusqueda','Debes introducir algún valor')
            self.add_error('fecha_desde','Debe introducir al menos un valor en un campo del formulario')
            self.add_error('fecha_hasta','Debe introducir al menos un valor en un campo del formulario')
            self.add_error('usuarios','Debe introducir al menos un valor en un campo del formulario')
            
        else:
            
            if (textoBusqueda != "" and len(textoBusqueda) < 3):
                self.add_error('textoBusqueda','Debe introducir al menos 3 caracteres')
            
            if(not fecha_desde is None  and not fecha_hasta is None and fecha_hasta < fecha_desde):
                self.add_error('fecha_desde','La fecha hasta no puede ser menor que la fecha desde')
                self.add_error('fecha_hasta','La fecha hasta no puede ser menor que la fecha desde')
                

        return self.cleaned_data


#LOGIN

class RegistroForm(UserCreationForm): 
    roles = (                   
                                (UsuarioLogin.TRABAJADOR, 'trabajador'),
                                (UsuarioLogin.CLIENTE, 'cliente'),
            )   
    rol = forms.ChoiceField(choices=roles)  
    class Meta:
        model = UsuarioLogin
        fields = ('username', 'email', 'password1', 'password2','rol')
        
class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ('moto','cliente')