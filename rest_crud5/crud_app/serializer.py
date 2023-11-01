from .models import City
from rest_framework import serializers

class SerializerCity(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'