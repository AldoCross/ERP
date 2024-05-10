from django.forms import ModelForm
from django import forms
from .models import Task, Producto, Cliente, Produccion, Ventas, Compras, H_R, Mantenimiento

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description', 'important']
        
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','ingreso','gasto']
        
class ClientesCRMfrom(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id','nombre','apellido1','apellido2','numero','correo','ventas_realizadas','cliente_importante']
        
class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['nombre', 'modelo', 'serie', 'NumeroOrden', 'cantidad']
        
class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['account','name','rep','manager','product','quantity','price','status']
        
class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['nombre', 'modelo', 'serie', 'NumeroOrden', 'cantidad', 'FechaCompra']
        
class HRForm(forms.ModelForm):
    class Meta:
        model = H_R
        fields = ['NumeroEmpleado', 'nombres', 'PrimerApellido', 'SegundoApellido', 'puesto', 'RFC', 'FechaIngreso']
        
class MantenimientoForm(ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['equipo', 'linea', 'fecha', 'tecnico', 'numero_empleado']

        