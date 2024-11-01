from django.urls import path 
from .views import RepuestosView,RepuestosUsuarioList,RepuestosDetallesList

urlpatterns = [
    path('cargar',RepuestosView.as_view(),name='formulariorepuestos'),
    path('',RepuestosUsuarioList.as_view(),name='listarepuestos'),
    path('detalle/<int:pk>/',RepuestosDetallesList.as_view(),name='detallerepuesto')     
]
