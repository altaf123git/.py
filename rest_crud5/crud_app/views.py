from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import SerializerCity
from .models import City

# # Create your views here.

@api_view(['POST'])
def Create(request):
    serializer=SerializerCity(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def Read(request):
    records=City.objects.all()
    serializer=SerializerCity(records, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def Update(request,id):
    record=City.objects.get(id=id)
    serializer=SerializerCity(instance=record, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_rocord(request,id):
    record=City.objects.get(id=id)
    record.delete()
    return Response('deleted')
    
@api_view(['GET'])
def show_record(request,id):
    record=City.objects.get(id=id)
    serializer=SerializerCity(record)
    return Response(serializer.data)

    