from django.db import models
from django.forms import EmailField

class Cliente(models.Model):

    nombre = models.CharField('nombre',max_length=30)
    apellido = models.CharField('apellido',max_length=30)
    edad = models.IntegerField('edad')
    email = models.EmailField('email')


class Gorra(models.Model):

    bordado = models.CharField('bordado',max_length=30)
    color = models.CharField('color',max_length=20)
    precio = models.FloatField('precio $')
    #foto = models.ImageField()

class Remera(models.Model):

    color = models.CharField('Color',max_length=20)
    estampado = models.CharField('Estampado',max_length=30)
    TALLES = (

        (1, 'S'),
        (2, 'M'),
        (3, 'XL'),
    ) 
    talle = models.SmallIntegerField('Talle',choices=TALLES)
    precio = models.FloatField('precio $')
    #foto = models.ImageField() 


