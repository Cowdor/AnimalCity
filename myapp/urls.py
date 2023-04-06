from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login),
    path('home', views.home),
    path('Agendar', views.Agendar),
    path('Funcionarios', views.Funcionarios),
    path('Paciente', views.Paciente),
    path('Resumen', views.Resumen),
    path('Productos', views.Productos),
    path('Ventas', views.Ventas),
    path('Historial_Cli', views.Historial_Cli),
]