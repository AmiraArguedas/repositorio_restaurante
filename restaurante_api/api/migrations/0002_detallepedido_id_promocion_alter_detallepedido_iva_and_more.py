# Generated by Django 5.1.2 on 2024-10-29 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepedido',
            name='id_promocion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.promocion'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='mesasestado',
            name='nombre_estado',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('reservada', 'Reservada'), ('Disponible', 'disponible'), ('Reservada', 'reservada')], max_length=50),
        ),
    ]
