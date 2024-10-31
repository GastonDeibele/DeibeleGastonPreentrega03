from django.urls import path 
from .views import ServiciosView,ServiciosUsuarioList

urlpatterns = [
    path('cargar',ServiciosView.as_view(),name='formularioservicios'),
    path('',ServiciosUsuarioList.as_view(),name='listaservicios')    
]
