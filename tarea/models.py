from django.db import models

# Create your models here.


class Tareas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    datecompleted = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=False)
   
class Invitado(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    relacion_personal = models.CharField(max_length=200)
    organizador = models.BooleanField(default=False)
