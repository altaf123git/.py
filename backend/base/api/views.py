from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    route=['name''jwt',
           'projec''first']
    #return JsonResponse(route, safe=False)
    return Response(route)