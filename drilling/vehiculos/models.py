from django.db import models
from django.contrib.auth.models import Permission

class Vehiculo(models.Model):
    Marca_Choices = [
        ('Ford', 'Ford'),
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Toyota', 'Toyota')
    ]
    Categoria_Choices = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]

    marca = models.CharField(max_length=20, choices=Marca_Choices, default='Ford')
    modelo = models.CharField(max_length=200)
    carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=Categoria_Choices, default='Particular')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    precio = models.IntegerField()
    imagen_url = models.URLField(blank=True)

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"),
        ]

