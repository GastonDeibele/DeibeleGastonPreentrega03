from django.db import models


    
class Maquinaria(models.Model):

    tipo=models.CharField(max_length=20)
    num_serie=models.CharField(unique=True,max_length=20)
    modelo=models.CharField(max_length=10)
    marca=models.CharField(max_length=20)
    hs_trabajo=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.num_serie}' 
    
    


# Create your models here.
