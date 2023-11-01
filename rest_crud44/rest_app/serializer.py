from .models import Message
from rest_framework import serializers
# from .tasks import file_resize

class MessageSerializer(serializers.ModelSerializer):
  class Meta():
    model = Message
    fields = "__all__"
