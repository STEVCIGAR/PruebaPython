from rest_framework import serializers
from productos.models import Producto, LugaresVenta, Precios

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Producto
        fields = "__all__"

class LugaresVentaSerializer(serializers.ModelSerializer):

    class Meta:

        model = LugaresVenta
        fields = "__all__"

class PreciosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Precios
        fields = "__all__"