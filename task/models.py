from django.db import models
from django.contrib.auth.models import User
# python manage.py makemigrations
#Este comando creará un archivo de migración para el modelo de la tabla

# python manage.py migrate
#este comando creará la tabla en la base de datos SQLite.

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
    
#base de datos para el modulo de Produccion
class Produccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    NumeroOrden = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    def _str_(self):
      return self.title + ' - by: ' + self.user.username

#base de datos para el modulo de Sales (ventas)
class Ventas(models.Model):
    account = models.IntegerField()
    name = models.CharField(max_length=255)
    rep = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    def _str_(self):
      return self.title + ' - by: ' + self.user.username
  
#base de datos para el modulo de compras
class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    NumeroOrden = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    FechaCompra = models.DateField(null=True, blank=True)
    def __str__(self):
        fecha_str = self.FechaCompra.strftime('%d/%m/%Y') if self.FechaCompra else ''
        return self.nombre + ' - FechaCompra: ' + fecha_str + ' - by: ' + self.user.username
        
#base de datos para el modulo de recursos humanos
class H_R(models.Model):
    NumeroEmpleado = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    PrimerApellido = models.CharField(max_length=50)
    SegundoApellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    RFC = models.CharField(max_length=50)
    FechaIngreso = models.DateField(null=True, blank=True)
    def __str__(self):
        fecha_str = self.FechaIngreso.strftime('%d/%m/%Y') if self.FechaIngreso else ''
        return self.nombres + ' - FechaIngreso: ' + fecha_str + ' - by: ' + self.user.username
        
#base de datos para el modulo de mantenimiento
class Mantenimiento(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated ID
    equipo = models.CharField(max_length=50, verbose_name="Equipo")  # Text field for equipment name
    linea = models.CharField(max_length=50, verbose_name="Linea")  # Text field for line name
    fecha = models.DateField(verbose_name="Fecha")  # Date field for maintenance date
    tecnico = models.CharField(max_length=50, verbose_name="Técnico")  # Text field for technician name
    numero_empleado = models.CharField(max_length=50, verbose_name="Número de Empleado")  # Text field for employee number
    def __str__(self):
        return f"Mantenimiento para {self.equipo} en {self.linea} realizado por {self.tecnico} el {self.fecha.strftime('%d/%m/%Y')}"

