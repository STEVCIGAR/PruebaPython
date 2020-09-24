from django.urls import path, include
from productos.views import ProductoView, LugaresVentaView, PreciosView

urlpatterns = [
    path('productos/', ProductoView.as_view()),
    path('Lugares/', LugaresVentaView.as_view()),
    path('Precios/', PreciosView.as_view()),
]