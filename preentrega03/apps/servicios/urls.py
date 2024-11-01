from django.urls import path 
from .views import ServiciosView,ServiciosUsuarioList,ServicioDetallesList

urlpatterns = [
    path('cargar',ServiciosView.as_view(),name='formularioservicios'),
    path('',ServiciosUsuarioList.as_view(),name='listaservicios'),
    path('detalle/<int:pk>/',ServicioDetallesList.as_view(),name='detalleservicio')     
]
