from rest_framework import serializers
from .models import Resources, ClusterInfo

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ('cpu', 'memory', 'created_at')       

class ClusterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterInfo
        fields = ('component_type', 'number_of_members')
