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

#antigua base de datos del BI
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
        
#base de datos para el modulo de mantenimiento
class Mantenimiento(models.Model):
    id = models.AutoField(primary_key=True)  
    equipo = models.CharField(max_length=50)
    linea = models.CharField(max_length=50)
    tecnico = models.CharField(max_length=50)
    numero_empleado = models.CharField(max_length=50)
    fecha = models.DateField(null=True, blank=True)
    def __str__(self):
        fecha_str = self.fecha.strftime('%d/%m/%Y') if self.fecha else ''
        return self.tecnico + ' - fecha: ' + fecha_str + ' - by: ' + self.user.username
        
#base de datos para el modulo de recursos humanos(ignorar este codigo)
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
        
#base de datos para el modulo de eventos:
class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    def __str__(self):
        fecha_str = self.fecha.strftime('%m/%d/%Y') if self.fecha else ''
        return f"{self.nombre} - {fecha_str} - Sala: {self.sala}"

#base de datos para el modulo de stock (actualizada):
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    modelo = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.CharField(max_length=50)
    def _str_(self):
     return self.title + ' - by: ' + self.user.username

#base de datos para recursos humanos, (actualizada):
class Humanos(models.Model):
    NumeroEmpleado = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=250)
    Apellido1 = models.CharField(max_length=250)
    Apellido2 = models.CharField(max_length=250)
    RFC = models.CharField(max_length=250)
    Puesto = models.CharField(max_length=250)
    fechaIngreso = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.Nombres} {self.Apellido1}"
        
#base de datos para el modulo de ventas:
class Sales(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    cantidad_vendida = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"Venta a {self.cliente} de {self.cantidad_vendida} {self.producto}"
    
#base de datos para el modulo de calidad:
class linea(models.Model):
    linea = models.CharField(max_length=50)
    def __str__(self):
        return self.linea

#base de datos para el modulo de calidad
class piloto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    linea = models.ForeignKey(linea, on_delete=models.CASCADE)
    
#base de datos para el modulo de proyectos
class proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    empleado = models.ForeignKey(Humanos, on_delete=models.CASCADE)
    
#base de datos para el modulo de marketing
class Medio(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Campania(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    medio = models.ForeignKey(Medio, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

#modelo de datos para las payroll
class Nomina(models.Model):
    empleado = models.ForeignKey(Humanos, on_delete=models.CASCADE)  # Relación con Humanos
    salario_diario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()  
    def __str__(self):
        return f"Nómina de {self.empleado.Nombres} {self.empleado.Apellido1}"