from django.db import models

class Repuestos(models.Model):

    tipo=models.CharField(max_length=20)
    num_serie=models.CharField(unique=True,max_length=20)
    categoria=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    cantidad=models.IntegerField()

    def __str__(self):
        return f'{self.categoria} {self.marca} {self.num_serie}' 

# Create your models here.
