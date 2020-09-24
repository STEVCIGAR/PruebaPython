
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from productos.models import Producto, LugaresVenta, Precios
from productos.serializer import ProductoSerializer, LugaresVentaSerializer, PreciosSerializer
# Create your views here.

class ProductoView(APIView):

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Producto.objects.create(**serializer.data)
            return Response(serializer.data, status=200)
        return Response(status=400)

    def get(self, request):
        query_set = Producto.objects.all()
        serializer = ProductoSerializer(query_set, many=True)
        return Response(serializer.data, status=200)

    def put(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            Producto.objects.filter(id_Producto=request.data['id_Producto']).update(nombre_Producto= request.data['nombre_Producto'],descripcion_Producto= request.data['descripcion_Producto'])
            return Response(status=201)
        return Response(status=400)

    def delete(self, request):
        Producto.objects.filter(id_Producto=request.data['id_Producto']).delete()
        return Response(status=204)

class LugaresVentaView(APIView):

    def post(self, request):
        serializer = LugaresVentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #LugaresVenta.objects.create(**serializer.data)
            return Response(serializer.data, status=200)
        return Response(status=400)
    
    def get(self, request):
        query_set = LugaresVenta.objects.all()
        serializer = LugaresVentaSerializer(query_set, many=True)
        return Response(serializer.data, status=200)

class PreciosView(APIView):

    def post(self, request):
        serializer = PreciosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Precios.objects.create(**serializer.data)
            return Response(serializer.data, status=200)
        return Response(status=400)

    def get(self, request):
        query_set = Precios.objects.all()
        serializer = PreciosSerializer(query_set, many=True)
        return Response(serializer.data, status=200)

    def put(self, request):
            Precios.objects.filter(id_Precio=request.data['id_Precio']).update(Precio_Precio= request.data['Precio_Precio'])
            return Response(status=201)
    
    def delete(self, request):
        Precios.objects.filter(id_Precio=request.data['id_Precio']).delete()
        return Response(status=204)
    