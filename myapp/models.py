from django.db import models


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_Persona = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.EmailField()
    tipo = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_persona})"

    class Meta:
        db_table = 'persona'

   


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre_Mascota = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    peso = models.FloatField()
    fecha_nac = models.DateField()
    estado_salud = models.CharField(max_length=45, blank=True, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'mascota'
        unique_together = (('id_mascota', 'persona'),)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.id_mascota) 


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_ven = models.DateField()
    cantidad = models.IntegerField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Ventas'
        unique_together = (('id_venta', 'persona'),)




class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_pro = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    precio = models.FloatField()
    stock = models.IntegerField()
    fecha_v = models.DateField()
    tipo_pro = models.IntegerField()

    class Meta:
        db_table = 'Productos'


class ConsultaMedica(models.Model):
    id_consulta_medica = models.AutoField(primary_key=True)
    fecha_con = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Consulta_Medica'
        unique_together = (('id_consulta_medica', 'mascota'),)


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Ventas_has_Productos'
        unique_together = (('venta', 'producto'),)