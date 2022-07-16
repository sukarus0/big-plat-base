from rest_framework import viewsets

from .models import BigDataComponent
from .serializers import BigDataComponentSerializer

# Create your views here.
class BigDataComponentViewSet(viewsets.ModelViewSet):
    queryset = BigDataComponent.objects.all()
    serializer_class = BigDataComponentSerializer
