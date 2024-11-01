from django.urls import path 
from .views import MaquinariaView,MaquinariaUsuarioList,MaquinariaDetallesList,ActualizarMaquinaria,EliminarMaquinaria

urlpatterns = [
    path('cargar',MaquinariaView.as_view(),name='formulariomaquinaria'),
    path('',MaquinariaUsuarioList.as_view(),name='listamaquinaria'),
    path('detalle/<int:pk>/',MaquinariaDetallesList.as_view(),name='detallemaquinaria'),
    path('actualizar/<int:pk>/',ActualizarMaquinaria.as_view(),name='updatemaquinaria'),
    path('eliminar/<int:pk>/',EliminarMaquinaria.as_view(),name='eliminarmaquinaria')     
        
]
