from django.forms import ModelForm
from .models import Maquinaria


class MaquinariaForms(ModelForm):

    class Meta: 

        model=Maquinaria
        
        fields= '__all__'