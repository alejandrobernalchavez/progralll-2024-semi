from django.db import models

# Create your models here.
class alumno(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)

class docente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=150)

class materia(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=75)
    uv = models.CharField(max_length=2)
<<<<<<< HEAD
    
=======
>>>>>>> 30438959c519b53811b049b7977a21b1616bd8c2
