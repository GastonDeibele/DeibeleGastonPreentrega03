from django.forms import ModelForm
from .models import Servicios


class ServiciosForms(ModelForm):

    class Meta: 

        model=Servicios
        
        fields= '__all__'