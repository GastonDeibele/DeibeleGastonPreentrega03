from django.shortcuts import render
from django.urls import reverse_lazy
from .form import ServiciosForms
from .models import Servicios
from django.views.generic import CreateView,ListView

class ServiciosView(CreateView):
    model=Servicios
    form_class=ServiciosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class ServiciosUsuarioList(ListView):
    model=Servicios   
    template_name='lista.html'

    context_object_name="objects"