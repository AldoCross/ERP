# Generated by Django 5.0.2 on 2024-04-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_cliente_producto_tabla_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=50)),
                ('NumeroOrden', models.CharField(max_length=50)),
                ('cantidad', models.CharField(max_length=50)),
            ],
        ),
    ]
