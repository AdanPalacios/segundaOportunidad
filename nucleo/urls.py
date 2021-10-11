from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('publicacion/', views.publicacion, name="publicacion"),
    path('registro/', views.registro, name="registro"),
    path('principal/', views.principal, name="principal"),
    path('buscarCuenta/', views.buscarCuenta, name="buscarCuenta"),
    path('info/', views.info, name="info"),
    path('perfil/', views.perfil, name="perfil"),
    path('editar/', views.editar, name="editar"),
    path('publicar/', views.publicar, name="publicar"),
    path('restablecer/', views.restablecer, name="restablecer"),
    path('editarCuenta/', views.editarCuenta, name="editarCuenta"),

]