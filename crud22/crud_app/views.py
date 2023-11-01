from django.shortcuts import render, redirect
from.models import Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/')
def create(request):
#     return render(request, 'main.html', {'data':data})
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        pan=request.FILES.get('pan')
        data=Employee(name=name, email=email, city=city, pan=pan)
        if data:
            data.save()
            messages.success(request, "Created Successfully!")
            return redirect('/create')
    else:
        data=Employee.objects.all()
        return render(request, 'main.html', {'data':data})
    return render(request, 'main.html')

def update_record(request,id):
    record=Employee.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        pan=request.FILES.get('pan')
        record.name=name
        record.email=email 
        record.city=city
        if pan:
            record.pan=pan
        record.save()
        messages.success(request, "Updated Successfully!")
    return render(request,'update.html', {'record':record})

def delete_record(request,id):
    record=Employee.objects.get(id=id)
    record.delete()
    messages.error(request, "Deleted Successfully!")
    return redirect('/create')


def user_register(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            new_admin=User.objects.create_user(uname, email, pass1)      
            messages.success(request, "New User Created Successfully!")
        else:
            messages.error(request, 'Password does not matched!')
    return render(request, 'new_user.html')

def user_login(request):
    if request.method=='POST':          
        user=request.POST.get('username')
        password=request.POST.get('password')
        admin=authenticate(username=user, password=password)
        if admin is not None:
            login(request, admin)
            return redirect('/create')
        else:
            messages.error(request, 'something is wrong')
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/')
    
# def read(request):
#     data=Employee.objects.all()
#     return render(request, 'main.html', {'data':data})