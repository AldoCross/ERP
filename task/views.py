from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError

from .forms import TaskForm, ProductoForm, ClientesCRMfrom, ProduccionForm
from .models import Task, Producto, Cliente, Produccion

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

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

@login_required
def eliminarProduccion(request, produccion):
    Produccion = Produccion.objects.get(produccion=produccion)
    produccion.delete()
    return render (request,'production.html')
    

@login_required 
def sales(request):
    return render(request, 'sales.html')

# views.py
def sales_chart(request):
    # Leer el archivo CSV y procesar los datos (igual que en la vista `sales`)
    df = pd.read_csv('data.csv', delimiter = ';')
    pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)
    # Crear las trazas para el gráfico
    trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declinada')], name='Declinada')
    trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pendiente')], name='Pendiente')
    trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presentada')], name='Presentada')
    trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'ganada')], name='Ganada')
    # Crear el layout del gráfico
    layout = go.Layout(title='Estado de orden por cliente', barmode='stack')
    # Crear la figura del gráfico
    figure = {
        'data': [trace1, trace2, trace3, trace4],
        'layout': layout
    }
    # Renderizar el gráfico con Dash
    app = dash.Dash(__name__)
    app.layout = html.Div(children=[
        dcc.Graph(id='sales-chart', figure=figure)
    ])
    # Obtener el HTML del gráfico
    graph_div = app.to_html(include_plotlyjs=False)
    # Renderizar el template 'sales.html' y pasar el HTML del gráfico
    context = {
        'graph_div': graph_div
    }
    return render(request, 'sales.html', context)


@login_required 
def HR(request):
    return render(request, 'HR.html')

@login_required 
def purchasing(request):
    return render(request, 'purchasing.html')

@login_required 
def maintenance(request):
    return render(request, 'maintenance.html')

#@login_required 
#def CRM(request):
#    return render(request, 'CRM.html')
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