from django import forms
from myapp .models import *

class formulario_Mascota(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


    opciones = [(1,'Macho'),(2,'Hembra')]
    sexo = forms.ChoiceField(choices= opciones)
    fecha_nac = forms.DateTimeField()

    class Meta:
        model = Mascota
        fields = ['nombre_Mascota','raza','sexo','peso','fecha_nac','estado_salud']
        
#####################################################################        
    
class formulario_Persona(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        model = Persona
        fields = ['nombre_Persona','apellido','direccion','telefono','correo','tipo']
    
        widgets = {
                'tipo':forms.HiddenInput()
            }
        
#####################################################################

class formulario_Funcionario(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    opciones = [(1,'1'),(2,'2')]
    tipo = forms.ChoiceField(choices= opciones)
    
    class Meta:
        model = Persona
        fields = ['nombre_Persona','apellido','direccion','telefono','correo','tipo']
    
        
#####################################################################

class formulario_Venta(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        model = Venta
        fields = ['fecha_ven','cantidad','persona']

#####################################################################

class formulario_producto(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        model = Producto
        fields = ['nombre_pro','descripcion','precio','stock','fecha_v','tipo_pro']

#####################################################################

class formulario_ConsultaM(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        model = ConsultaMedica
        fields = ['fecha_con','mascota']

#####################################################################

class formulario_VentaP(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    
    class Meta:
        model = VentaProducto
        fields = ['venta','producto']