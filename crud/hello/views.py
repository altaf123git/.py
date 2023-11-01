from django.shortcuts import render, HttpResponse, redirect
from hello.models import *
from django.contrib import messages #import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        dob=request.POST.get('dob')
        adhaar=request.FILES.get('adhaar')
        
        try:       
            Employee.objects.create(name=name, email=email, city=city, dob=dob, adhaar=adhaar)
            messages.success(request, "New Data Added Successfully!" )

        except:
            raise Exception
    return render(request, 'create.html')

def read(request):
    data=Employee.objects.all()
    return render(request, 'read.html', {'data':data})

def update(request, id):
    record=Employee.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        city=request.POST.get('city')
        dob=request.POST.get('dob')
        adhaar=request.FILES.get('adhaar')
        record.name=name
        record.email=email
        record.city=city
        # email=email 
        # city=city
        if dob:
            record.dob=dob
        if adhaar:
            record.adhaar=adhaar
        record.save()
        messages.success(request, "Record Updated Successfully!" )
    return render(request, 'update.html', {'record':record})

def delete_rec(request, id):
    record=Employee.objects.get(id=id)
    record.delete()
    messages.error(request, "Record Deleted Successfully!" )
    return redirect('/read')