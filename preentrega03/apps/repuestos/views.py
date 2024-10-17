from django.shortcuts import render
from django.urls import reverse_lazy
from .form import RepuestosForms
from .models import Repuestos
from django.views.generic import CreateView

class RepuestosView(CreateView):
    model=Repuestos
    form_class=RepuestosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')