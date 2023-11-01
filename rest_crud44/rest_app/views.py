from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializer import MessageSerializer
# Create your views here.

@api_view(['POST'])
def create(request):
    data=MessageSerializer(data=request.data)
    if data.is_valid():
        data.save()
    return Response(request.data)

@api_view(['GET'])
def read(request):
    data=Message.objects.all()
    serializer=MessageSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update(request,id):
    record=Message.objects.get(id=id)
    serializer=MessageSerializer(instance=record, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_rcord(request,id):
    record=Message.objects.get(id=id)
    record.delete()
    return Response('deleted')