from rest_framework import viewsets

from .models import Resources, ClusterInfo
from .serializers import ResourceSerializer, ClusterInfoSerializer

# Create your views here.
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer

class ClusterInfoViewSet(viewsets.ModelViewSet):
    queryset = ClusterInfo.objects.all()
    serializer_class = ClusterInfoSerializer
