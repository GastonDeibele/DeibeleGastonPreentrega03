from django.urls import path 
from .views import RepuestosView

urlpatterns = [
    path('',RepuestosView.as_view(),name='formulariorepuestos')    
]
