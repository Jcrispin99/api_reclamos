from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaimViewSet

# Crear un router para manejar las rutas automáticamente
router = DefaultRouter()
router.register(r'claims', ClaimViewSet, basename='claim')

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas generadas por el router
]