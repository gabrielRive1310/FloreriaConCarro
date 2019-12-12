from django.db import models

# Create your models here.

class Estado(models.Model):
    nombre_estado = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre_estado

class Flor(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=50, primary_key=True)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
    stock = models.IntegerField() 

    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    usuario=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    valor=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()
    fecha=models.DateField()

    def __str__(self):
        return str(self.usuario)+' '+str(self.nombre)


