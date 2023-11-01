from .models import Emp
from rest_framework import serializers

class SerializerEmp(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields=['name','email']