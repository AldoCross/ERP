from django.db import models
from django.contrib.auth.models import User

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
