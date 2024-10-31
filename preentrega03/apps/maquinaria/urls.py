from django.urls import path 
from .views import MaquinariaView,MaquinariaUsuarioList

urlpatterns = [
    path('cargar',MaquinariaView.as_view(),name='formulariomaquinaria'),
    path('',MaquinariaUsuarioList.as_view(),name='listamaquinaria')
        
]
