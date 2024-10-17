from django.forms import ModelForm
from .models import Repuestos


class RepuestosForms(ModelForm):

    class Meta: 

        model=Repuestos
        
        fields= '__all__'