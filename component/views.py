from rest_framework import viewsets

from .models import Resources
from .serializers import ResourceSerializer

# Create your views here.
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer
