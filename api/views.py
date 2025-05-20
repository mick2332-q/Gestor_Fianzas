from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categoria, Transaccion
from .serializers import CategoriaSerializer, TransaccionSerializer
from .filters import TransaccionFilter, CategoriaFilter

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriaFilter

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class=  TransaccionFilter

    ordering_fields = ['fecha', 'monto'] # Campos por los que se puede ordenar
    ordering = ['-created_at'] # Orden por defecto