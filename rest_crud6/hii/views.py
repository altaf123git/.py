from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import StudentSerializer
from .models import Student


# Create your views here.
@api_view(['GET'])
def home(request):
    data=Student.objects.all()
    serializer=StudentSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update(request,id):
    record=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=record, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['DELETE'])
def data_delete(request,i):
    record=Student.objects.get(pk=i)
    record.delete()
    return Response('deleted')

@api_view(['GET'])
def details_id(rquest,id):
    record=Student.objects.get(id=id)
    serializer=StudentSerializer(record)
    return Response(serializer.data)
    