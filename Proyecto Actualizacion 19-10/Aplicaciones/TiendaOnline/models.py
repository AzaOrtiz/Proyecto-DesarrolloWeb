from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class computadora(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.CharField(max_length=300)
    tipo = models.ForeignKey(
        'tipocompu',
        on_delete = models.CASCADE,
        default=1
        )    
    modelo = models.CharField(max_length=200) 
    precio = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    marca = models.ForeignKey(
        'marca',
        on_delete = models.CASCADE,
        default=1
        )    
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class marca(models.Model):
    marca = models.CharField(max_length=30)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.marca)

class tipocompu(models.Model):
    tipo = models.CharField(max_length=30)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):  
        return '%s' % (self.tipo)

class accesorio(models.Model):
    nombrea = models.CharField(max_length=200)
    tipoa = models.ForeignKey(
        'tipoacces',
        on_delete = models.CASCADE,
        default=1
        )    
    fotoa = models.CharField(max_length=300)
    precioa = models.CharField(max_length=200)
    descripciona = models.CharField(max_length=200)
    marcaa = models.ForeignKey(
        'marca',
        on_delete = models.CASCADE,
        default=1
        )    
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombrea)

class tipoacces(models.Model):
    tipo = models.CharField(max_length=30)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):  
        return '%s' % (self.tipo)

class imgMarcas(models.Model):
    nombrei = models.CharField(max_length=40, default="")
    fotoi = models.CharField(max_length=300)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):  
        return '%s' % (self.nombrei)