from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la categoría (ej. Comida, Transporte)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    TIPO_CHOICES = (
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   # Usuario dueño de la transacción
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # Tipo de transacción
    descripcion = models.TextField(blank=True)                    # Descripción opcional
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Valor monetario
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # Categoría opcional
    fecha = models.DateField()                                    # Fecha en la que ocurrió
    created_at = models.DateTimeField(auto_now_add=True)          # Fecha de creación del registro

    def __str__(self):
        return f"{self.tipo} - ${self.monto} - {self.fecha}"

