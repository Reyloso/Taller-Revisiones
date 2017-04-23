from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Consecionario(models.Model):
    nit = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono =models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)


class Auto(models.Model):
    Color = (
                ('Verde', 'Verde'),
                ('Azul', 'Azul'),
                ('Rojo', 'Rojo'),
                ('Amarillo', 'Amarillo'),
          )

    marca = models.CharField(max_length=50)
    tipo =  models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    consecionario = models.ForeignKey(Consecionario)
    matricula =  models.CharField(max_length=25)
    color = models.CharField(max_length=50,choices=Color)


    def __unicode__(self):
        return unicode(self.id)

class Cliente(models.Model):
    nid = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    auto = models.ForeignKey(Auto)

    def __unicode__(self):
        return unicode(self.nid)

class Revision(models.Model):
    Estado = (
            ('SI','SI'),
            ('NO','NO')
    )

    auto = models.ForeignKey(Auto)
    filtro = models.CharField(max_length=50,choices=Estado)
    aceite = models.CharField(max_length=50,choices=Estado)
    frenos = models.CharField(max_length=50,choices=Estado)
    motor = models.CharField(max_length=50,choices=Estado)

    def __unicode__(self):
        return unicode(self.id)
