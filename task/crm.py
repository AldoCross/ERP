from django.shortcuts import render
from .models import Cliente


def clientes_lista(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'CRM.html', context)
