from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError

from .forms import TaskForm, ProductoForm, ClientesCRMfrom, ProduccionForm, VentasForm, ComprasForm, HRForm
from .models import Task, Producto, Cliente, Produccion, Ventas, Compras, H_R

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# librerias para el modulo de sales

# AQUI SE CREAN LOS VIEWS BASICOS DE LA PAGINA WEB:
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
         'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
               return render(request,'signup.html',{
                'form': UserCreationForm,
                "error": 'User already Exist'
               })
            
        return render(request, 'signup.html',{
                'form': UserCreationForm,
                "error": 'User already Exists'
        })
        
@login_required        
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'tasks.html',{'tasks': tasks}) #funcion task

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'tasks.html',{'tasks': tasks}) #funcion task

@login_required
def create_task(request): #funcion para create_task
  if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form': TaskForm
        })
  else:
      try:
          form = TaskForm(request.POST)
          new_task = form.save(commit=False)
          new_task.user = request.user
          new_task.save()
          return redirect('tasks')
      except ValueError:
          return render(request, 'create_task.html',{
              'form': TaskForm,
              'error': 'Please provide valid data' 
          })
          
@login_required          
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task' : task, 'form' : form})
    else:
       try:
          task = get_object_or_404(Task, pk=task_id, user=request.user)
          form = TaskForm(request.POST, instance=task)
          form.save()
          return redirect('tasks')
       except ValueError:
           return render(request, 'task_detail.html', {'task':task, 'form':form, 'error': "Error updating task"})
      
@login_required           
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
  
@login_required  
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('home')
          
@login_required   
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
       return render(request, 'signin.html',{
       'form': AuthenticationForm
       })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request,user)
            return redirect('tasks')
        
#APARTIR DE AQUI SE CREAN LOS MODULOS ESPECIFICOS DE LA PAGINA WEB:
@login_required 
def finance(request):
    return render(request, 'finance.html')

@login_required 
def accounting(request):
    return render(request, 'accounting.html')

@login_required
def production(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            produccion = form.save()  # Omite el argumento 'id'
            # Actualizar el objeto con datos de la base de datos
            produccion.refresh_from_db()
            return redirect('production')
    else:  # Solicitud GET
        form = ProduccionForm()  # Instanciar el formulario
        produccion = Produccion.objects.all()  # Obtener todas las órdenes de producción
    return render(request, 'production.html', {'form': form, 'produccion': produccion})

from django.shortcuts import render
from django.contrib import messages
import plotly
import plotly.graph_objs as go
import json
from django.db import models
from django.contrib import messages
from .forms import VentasForm
from .models import Ventas
import pandas as pd
@login_required
def sales(request):
    if request.method == 'POST':
        if 'file' in request.FILES:  # Verificar si se cargó un archivo
            file = request.FILES['file']
            if file.name.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file)
                    table_data = df.to_dict('records')

                    # Procesar datos para el gráfico a partir de los datos cargados (modificar según sus necesidades)
                    product_counts = df['Productos'].value_counts()
                    bar_chart = go.Bar(x=product_counts.index, y=product_counts.values)
                    chart_data = json.dumps([bar_chart], cls=plotly.utils.PlotlyJSONEncoder)

                    return render(request, 'sales.html', {'table_data': table_data, 'chart_data': chart_data})
                except Exception as e:
                    messages.error(request, f"Error al procesar el archivo Excel: {str(e)}")
            else:
                messages.error(request.message, "El archivo debe tener formato .xlsx")
        else:
            form = VentasForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Venta guardada exitosamente!')
            else:
                messages.error(request.message, 'Error al guardar la venta')

    # Recuperar datos de la base de datos (sin cambios)
    ventas = Ventas.objects.all()
    table_data = ventas.values('account', 'name', 'rep', 'manager', 'product', 'quantity', 'price', 'status')
    product_counts = ventas.values('product').annotate(count=models.Count('product'))
    bar_chart = go.Bar(x=[p['product'] for p in product_counts], y=[p['count'] for p in product_counts])
    chart_data = json.dumps([bar_chart], cls=plotly.utils.PlotlyJSONEncoder)
    return render(request, 'sales.html', {'table_data': table_data, 'chart_data': chart_data})

@login_required
def HR(request):
    return render(request, 'HR.html')


@login_required
def purchasing(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            compra = form.save()  # Omite el argumento 'id'
            # Actualizar el objeto con datos de la base de datos
            compra.refresh_from_db()
            return redirect('purchasing')
    else:  # Solicitud GET
        form = ComprasForm()  # Instanciar el formulario
        compras = Compras.objects.all()  # Obtener todas las órdenes de compras
        return render(request, 'purchasing.html', {'form': form, 'compras': compras})


#@login_required 
#def maintenance(request):
#    return render(request, 'maintenance.html')
from .forms import MantenimientoForm
from .models import Mantenimiento
def maintenance(request):
  if request.method == 'POST':
    form = MantenimientoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('maintenance')  # Redirect to itself after saving
  else:
    form = MantenimientoForm()
  mantenimientos = Mantenimiento.objects.all()  # Get all maintenance records
  return render(request, 'maintenance.html', {'form': form, 'mantenimientos': mantenimientos})


@login_required
def CRM(request):
    if request.method == 'POST':
        form = ClientesCRMfrom(request.POST)
        if form.is_valid():
            # Save the new client to the database
            form.save()
            messages.success(request, '¡Cliente guardado exitosamente!')
            # Redirect back to the CRM page after successful saving
            return redirect('/CRM/')
        else:
            messages.error(request, '¡Hubo un error al guardar el cliente!')
    else:
        # Initialize an empty form for adding new clients
        form = ClientesCRMfrom()
    # Get all existing clients to display in the list
    clientes = Cliente.objects.all()
    # Render the CRM template with the form and list of clients
    return render(request, 'CRM.html', {
        'form': form,
        'clientes': clientes
    })

@login_required
def BI(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
    else:
        form = ProductoForm()
        productos = Producto.objects.all()  # Obtener todos los productos incluso para solicitudes GET

    return render(request, 'BI.html', {
        'form': form,
        'productos': productos,  # Agregar productos al contexto
    })

def quality(request):
    return render(request, 'quality.html')

def Ecommerce(request):
    return render(request, 'Ecommerce.html')

def payroll(request):
    return render(request, 'payroll.html')

def POS(request):
    return render(request, 'POS.html')

def Projects(request):
    return render(request, 'Projects.html')

def marketing(request):
    return render(request, 'marketing.html')