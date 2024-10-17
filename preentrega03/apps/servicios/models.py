from django.db import models

class Servicios(models.Model):

    cliente=models.CharField(max_length=20)
    maquina=models.CharField(max_length=20)
    num_serie=models.CharField(unique=True,max_length=20)
    tecnico=models.CharField(max_length=20)
    campo=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cliente} {self.maquina} {self.tecnico}' 
    


# Create your models here.
