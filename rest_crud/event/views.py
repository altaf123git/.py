from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def employeeList(request):
    employees=Employee.objects.all()
    serializer=EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def employeeUpdate(request,id):
    employee=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def employeeDelete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()    
    
    return Response('Deleted')

@api_view(['GET'])
def employeeDetail(request,id):
    employee=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(employee)
    return Response(serializer.data)

# Create your views here.
