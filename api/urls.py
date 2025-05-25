from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TransaccionViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterViewSet.as_view(), name='register'),
]
