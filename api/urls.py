from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TransaccionViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')

urlpatterns = router.urls
