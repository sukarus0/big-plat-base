from rest_framework import serializers
from .models import Resources

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ('cpu', 'memory', 'created_at')       
