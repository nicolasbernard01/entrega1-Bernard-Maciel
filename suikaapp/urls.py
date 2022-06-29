from django.urls import path
from . import views

urlpatterns = [
    #path('', views.hola, name='index'),
    path('', views.inicio, name='inicio'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('nuevo_gorro/', views.nuevo_gorro, name='nuevo_gorro'),
    path('nueva_remera/', views.nueva_remera, name='nueva_remera'),
    path('clientes/', views.clientes, name='clientes'),
    path('buscar_gorra/', views.buscar_gorra, name='buscar_gorra'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar_remera/', views.buscar_remera, name='buscar_remera')

]