"""
URL configuration for ERPproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views #importamos el archivo views de la carpeta task

urlpatterns = [
    #URLS basicos:
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    
    #URLS de los modulos:
    path('finance/', views.finance, name='finance'),
    path('accounting/', views.accounting, name='accounting'),
    
    path('production/', views.production, name='production'),
    path('sales/', views.sales_chart, name='sales'),
    
    path('HR/', views.HR, name='HR'),
    path('purchasing/', views.purchasing, name='purchasing'),
    path('maintenance/', views.maintenance, name='maintenance'),
    
    path('CRM/', views.CRM, name='CRM'),
    path('BI/', views.BI, name='BI'),
   
    path('quality/', views.quality, name='quality'),
    path('Ecommerce/', views.Ecommerce, name='Ecommerce'),
    path('payroll/', views.payroll, name='payroll'),
    path('POS/', views.POS, name='POS'),
    path('Projects/', views.Projects, name='Projects'),
    path('marketing/', views.marketing, name='marketing'),
]