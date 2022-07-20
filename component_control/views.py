from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ComponentStatus
from .serializers import ComponentStatusSerializer

# Create your views here.
class ComponentStatusViewSet(viewsets.ModelViewSet):
    queryset = ComponentStatus.objects.all()
    serializer_class = ComponentStatusSerializer


@api_view(['GET', 'POST'])
def startComponent(request):
    if request.method == 'GET':
        return Response("Component Started.")
    elif request.method == 'POST':
        return Response(f"Component Started with options : {request.data}")

@api_view(['GET', 'POST'])
def stopComponent(request):
    if request.method == 'GET':
        return Response("Component Stopped.")
    elif request.method == 'POST':
        return Response(f"Component Stopped with options : {request.data}")

@api_view(['GET', 'POST'])
def restartComponent(request):
    if request.method == 'GET':
        return Response("Component Restarted.")
    elif request.method == 'POST':
        return Response(f"Component Restarted with options : {request.data}")
