# Generated by Django 5.0.2 on 2024-05-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_product_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Humanos',
            fields=[
                ('NumeroEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=250)),
                ('Apellido1', models.CharField(max_length=250)),
                ('Apellido2', models.CharField(max_length=250)),
                ('RFC', models.CharField(max_length=250)),
                ('Puesto', models.CharField(max_length=250)),
                ('fechaIngreso', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
