from django.db import models

# Create your models here.

class Producto(models.Model):

    id_Producto = models.AutoField(primary_key=True)
    nombre_Producto = models.CharField(max_length=30)
    descripcion_Producto = models.CharField(max_length=300)

class LugaresVenta (models.Model):

    id_LVenta = models.AutoField(primary_key=True)
    nombre_LVenta = models.CharField(max_length=30)
    ubicacion_LVenta = models.CharField(max_length=50)

class Precios (models.Model):

    id_Precio = models.AutoField(primary_key=True)
    fk_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Precio_Precio = models.FloatField()
    Presentacion_Precio = models.CharField(max_length=30)
    fk_LVenta = models.ForeignKey(LugaresVenta, on_delete=models.CASCADE)
