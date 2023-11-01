from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view(['GET'])
# def read(request):
#     std=Student.objects.all()
#     serializer=SerializerStudent(std, many=True) 
#     return Response(serializer.data)

@api_view(['GET'])
def studentList(request):
    std=Student.objects.all()
    serializer=StudentSerializer(std, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def studentCreate(request):
    record=StudentSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['GET'])
def studentDetail(request, id):
    std=Student.objects.get(id=id)
    serializer=StudentSerializer(std)
    return Response(serializer.data)

@api_view(['POST'])    
def studentUpdate(request, id):
    std=Student.objects.get(id=id)
    record=StudentSerializer(instance=std, data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)

@api_view(['DELETE'])
def studentDelete(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return Response('Deleted')

