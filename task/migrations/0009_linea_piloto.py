# Generated by Django 5.0.2 on 2024-05-17 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.linea')),
            ],
        ),
    ]
