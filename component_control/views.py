from rest_framework import viewsets

from .models import ComponentStatus
from .serializers import ComponentStatusSerializer

# Create your views here.
class ComponentStatusViewSet(viewsets.ModelViewSet):
    queryset = ComponentStatus.objects.all()
    serializer_class = ComponentStatusSerializer
