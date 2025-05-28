from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TransaccionViewSet,RegisterView

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
