from django.shortcuts import render
from django.urls import reverse_lazy
from .form import ServiciosForms
from .models import Servicios
from django.views.generic import CreateView

class ServiciosView(CreateView):
    model=Servicios
    form_class=ServiciosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')