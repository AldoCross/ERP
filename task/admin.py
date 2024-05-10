from django.contrib import admin
from .models import Task, Producto, Cliente, Produccion, Ventas, Compras, H_R
from .models import Mantenimiento
#aqui en este codigo, se agregan las tablas de las bases de datos
#que creamos en models.py para que el admin tenga acceso a ellas.

#clase para mostrar la fecha de creacion de la tarea, desde el admin de Django.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

#creacion de administrador de tareas del admin de Django.
admin.site.register(Task, TaskAdmin)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Produccion)
admin.site.register(Ventas)
admin.site.register(Compras)
#admin.site.register(H_R)
admin.site.register(Mantenimiento)