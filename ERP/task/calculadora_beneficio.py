from django.db import models
from django.shortcuts import render
from .models import Producto
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    ingreso = models.DecimalField(max_digits=10, decimal_places=2)
    gasto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    def calcular_beneficio(self):
        return self.ingreso - self.gasto
      
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ingreso = float(request.POST['ingreso'])
        gasto = float(request.POST['gasto'])

        producto = Producto(nombre=nombre, ingreso=ingreso, gasto=gasto)
        producto.save()

        productos = Producto.objects.all()
        beneficio_total = sum(producto.calcular_beneficio() for producto in productos)

        return render(request, 'BI.html', {'productos': productos, 'beneficio_total': beneficio_total})
    else:
        return render(request, 'BI.html')

def calcular_beneficio(request):
    if request.method == 'POST':
        producto_id = int(request.POST['producto_id'])
        producto = Producto.objects.get(id=producto_id)
        beneficio = producto.calcular_beneficio()

        return JsonResponse({'beneficio': beneficio})
    else:
        return HttpResponseBadRequest()