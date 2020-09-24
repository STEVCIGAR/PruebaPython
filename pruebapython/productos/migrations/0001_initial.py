# Generated by Django 3.1.1 on 2020-09-24 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LugaresVenta',
            fields=[
                ('id_LVenta', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_LVenta', models.CharField(max_length=30)),
                ('ubicacion_LVenta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_Producto', models.CharField(max_length=30)),
                ('descripcion_Producto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id_Precio', models.AutoField(primary_key=True, serialize=False)),
                ('Precio_Precio', models.FloatField()),
                ('Presentacion_Precio', models.CharField(max_length=30)),
                ('fk_LVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.lugaresventa')),
                ('fk_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]