from rest_framework import serializers
from .models import ComponentStatus

class ComponentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentStatus
        fields = ('name', 'status')
