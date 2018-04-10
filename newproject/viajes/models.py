from django.db import models

# Create your models here.

class Viaje(models.Model):
    destino = models.CharField(max_length = 32)
    locomocion = models.CharField(max_length = 32)
    alojamiento = models.CharField(max_length = 32)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.destino



class Cliente(models.Model):
    nombre = models.CharField(max_length = 32)
    dni =  models.CharField(max_length = 32)
    nacimiento = models.DateField()
    viaje = models.ForeignKey(Viaje)
    def __str__(self):
        return self.nombre
