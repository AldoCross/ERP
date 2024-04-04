from django.db import models
from django.contrib.auth.models import User
#python manage.py makemigrations
#Este comando creará un archivo de migración para el modelo Producto.

#python manage.py migrate
#este comando creará la tabla producto en la base de datos SQLite.

# Create your models here, aqui se hacen las tablas para la base de datos.
class Task(models.Model): #Tabla Tareas
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def _str_(self):
        return self.title + ' - by: ' + self.user.username

#base de datos del BI
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    ingreso = models.DecimalField(max_digits=10, decimal_places=2)
    gasto = models.DecimalField(max_digits=10, decimal_places=2)
    tabla_productos = models.TextField(blank=True, null=True)
    def _str_(self):
        return self.title + ' - by: ' + self.user.username
    def __str__(self):
        return self.nombre
    def calcular_beneficio(self):
        return self.ingreso - self.gasto

#base de datos del CRM
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    correo = models.EmailField()
    ventas_realizadas = models.IntegerField()
    cliente_importante = models.BooleanField()
    def _str_(self):
      return self.title + ' - by: ' + self.user.username
    
    

