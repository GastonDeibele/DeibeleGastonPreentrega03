from django.urls import path 
from .views import RepuestosView,RepuestosUsuarioList

urlpatterns = [
    path('cargar',RepuestosView.as_view(),name='formulariorepuestos'),
    path('',RepuestosUsuarioList.as_view(),name='listarepuestos')    
]
