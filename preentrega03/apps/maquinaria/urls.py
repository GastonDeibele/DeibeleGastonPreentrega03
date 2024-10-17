from django.urls import path 
from .views import MaquinariaView

urlpatterns = [
    path('',MaquinariaView.as_view(),name='formulariomaquinaria')    
]
