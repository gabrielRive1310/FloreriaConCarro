from django.urls import path
from django.contrib import admin
from .views import home, contacto, tienda, registro_usuario,grabar_carro,carros,carro_compras_mas,carro_compras_menos,agregar_carrito,carrito,vaciar_carrito

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto" ),
    path('tienda/', tienda, name="tienda"),
    path('registro/', registro_usuario, name="registro_usuario"),
    path('agregar_carrito/<id>/',agregar_carrito,name='AGREGARCARRITO'),
    path('carro/',carros,name='CARRITO1'),
    path('carro_mas/<id>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
    path('carrito/',carrito,name='CARRITO'),
    path('vaciar_carrito/',vaciar_carrito,name='VACIARCARRITO'),
]
