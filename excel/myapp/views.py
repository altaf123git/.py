from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
import csv
from django.db.models import Q
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'index.html')

def new_user(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=CustomUser.objects.create_user(email=email, password=password)
        if user is not None:
            user.save()
            return HttpResponse('created')
    return render(request, 'register.html')


def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')   
        user=authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/excel')  
        else:
            return HttpResponse('something goes wrong')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

import pandas as pd
import json

# @login_required(login_url='login')
# def upload_excel(request):
#     context=dict()
#     if request.method=='POST':
#         file_csv=request.FILES.get('excel_file')
#         df=pd.read_csv(file_csv)
#         json_records = df.reset_index().to_json(orient ='records') 
#         data = [] 
#         data = json.loads(json_records) 
#         context = {'d': data}    
#         print(data)   
#     return render(request, 'excel.html', context)

@login_required(login_url='login')
def upload_excel(request):
    context=dict()
    if request.method=='POST':
        file_csv=request.FILES.get('excel_file')
        df=pd.read_csv(file_csv)
        json_records = df.reset_index().to_json(orient ='records') 
        print('jsonnnnn',json_records)
        data = [] 
        data = json.loads(json_records) 
        print('dataaaa',data)
        context = {'d': data}    
        print('contextttt',context)   
    return render(request, 'excel.html', context)
