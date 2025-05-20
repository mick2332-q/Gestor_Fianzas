import django_filters
from .models import Transaccion, Categoria
from django.contrib.auth.models import User

class CategoriaFilter(django_filters.FilterSet):
    # Filtro por nombre de categoría (parcial)
    nombre= django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    
    categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(),
        label="Categoría"
    )

    class Meta:
        model = Categoria
        fields = []


class TransaccionFilter(django_filters.FilterSet):
    usuario = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Usuario"
    )
    tipo = django_filters.ChoiceFilter(
        choices=Transaccion.TIPO_CHOICES,
        label="Tipo"
    )
    categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(),
        label="Categoría"
    )
    min_monto = django_filters.NumberFilter(field_name='monto', lookup_expr='gte')
    max_monto = django_filters.NumberFilter(field_name='monto', lookup_expr='lte')
    fecha_inicio = django_filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_fin = django_filters.DateFilter(field_name='fecha', lookup_expr='lte')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')

    class Meta:
        model = Transaccion
        fields = []