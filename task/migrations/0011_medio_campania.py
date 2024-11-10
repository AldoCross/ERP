# Generated by Django 5.0.2 on 2024-05-20 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_proyectos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Campania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.medio')),
            ],
        ),
    ]
