from django.db import models
#Crear bases de datos en este espacio
# Create your models here.
class Project(models.Model): 
#Dentro de la carpeta models llamo la clase Model, Se crea una tabla en la base de datos llamada models
    name = models.CharField(max_length=200)
    age = models.FloatField()

    def __str__(self):
        return self.name #Nos permite ver el contenido desde el panel administrador

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Con esto estaria relacionando las tablas project y task, models.CASCADE permite que se elimine lo relacionado con lo que se elimine
    done = models.BooleanField(default=False) #Añadimos dentro de la tabla un campo donde los valores solo pueden ser booleanos

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Viaje(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    conductor = models.CharField(max_length=100)
    hora_llegada = models.CharField(max_length=100)