from django.contrib import admin
from .models import Persona, Mascota, Venta, Producto, ConsultaMedica, VentaProducto
# Register your models here.

admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(ConsultaMedica)
admin.site.register(VentaProducto)

