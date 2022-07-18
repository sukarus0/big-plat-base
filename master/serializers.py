from rest_framework import serializers
from .models import BigDataComponent

class BigDataComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigDataComponent
        fields = ('category', 'name', 'access_point')
