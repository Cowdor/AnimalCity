from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('menu', views.menu),
    path('reg_funcionarios', views.reg_funcionarios, name = 'funcionarios'),
    path('reg_productos', views.reg_productos, name = 'productos'),
    path('reg_mascota', views.reg_mascota, name = 'mascotas'),
    path('vista', views.vista),
    # path('historias2', views.registrar2),
]