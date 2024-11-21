from django.shortcuts import render
from django.urls import reverse_lazy
from .form import RepuestosForms
from .models import Repuestos
from django.views.generic import CreateView,ListView,DetailView


class RepuestosView(CreateView):
    model=Repuestos
    form_class=RepuestosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class RepuestosUsuarioList(ListView):
    model=Repuestos   
    template_name='lista.html'

    context_object_name="objects"
    def get_context_data(self, **kwargs):

        context_data= super().get_context_data(**kwargs)
        context_data["urldetail"]="detallerepuesto"
        context_data["url_add"] = "formulariorepuestos"
        return context_data
        

    def get(self, request, *args, **kwargs):
        inputuser = self.request.GET.get("input_name", "")
        queryset = self.get_queryset().filter(num_serie__icontains=inputuser) 
        self.queryset=queryset
        
        return super().get(request, *args, **kwargs)
    
class RepuestosDetallesList(DetailView):
    model=Repuestos
    template_name='detallerepuesto.html'

    context_object_name="repuesto"
