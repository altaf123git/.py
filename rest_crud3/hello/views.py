from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import SerializerEmp
from .models import Emp
# Create your views here.

@api_view(['POST'])
def Create(request):
    serializer=SerializerEmp(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def Read(request):
    records=Emp.objects.all()
    serializer=SerializerEmp(records, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Update(request,id):
    record=Emp.objects.get(id=id)
    serializer=SerializerEmp(instance=record, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def Deletedata(request,id):
    record=Emp.objects.get(id=id)
    record.delete()
    return Response('deleted')

@api_view(['GET'])
def Data(request,id):
    record=Emp.objects.get(id=id)
    serializer=SerializerEmp(record)
    return Response(serializer.data)
    
    