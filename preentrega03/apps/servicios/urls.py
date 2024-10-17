from django.urls import path 
from .views import ServiciosView

urlpatterns = [
    path('',ServiciosView.as_view(),name='formularioservicios')    
]
