from django.shortcuts import render
from django.urls import reverse_lazy
from .form import MaquinariaForms
from .models import Maquinaria
from django.views.generic import CreateView

class MaquinariaView(CreateView):
    model=Maquinaria
    form_class=MaquinariaForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

# Create your views here.
