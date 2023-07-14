from django.urls import path
from .views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', index),
    path('vehiculo/add/', crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/lista/',catalogo, name='listado_vehiculos'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='inicio_sesion.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('vehiculo/<int:vehiculo_id>/', detalle_vehiculo, name='detalle_vehiculo'),
]
