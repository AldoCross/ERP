from django.forms import ModelForm
from django import forms
from .models import Task, Producto, Cliente

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
