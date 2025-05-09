from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Claim
from .serializers import ClaimSerializer

class ClaimViewSet(ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD del modelo Claim.
    """
    queryset = Claim.objects.all()  # Define los datos que se manejarán
    serializer_class = ClaimSerializer  # Usa el serializador que creaste
# Create your views here.
