from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def admin_site(request):
    return render(request, 'admin.html')

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        course=request.POST.get('course')
        college=request.POST.get('college')
        idc=request.FILES.get('idc')
        mail=request.POST.get('mail')
        try:
            new_data=Student(name=name, mail=mail, course=course, college=college, id_card=idc)
            if new_data:
                new_data.save()
                messages.success(request, 'New Data Added Successfully!')
        except:
            return HttpResponse('something got wrong')
    return render(request, 'create.html')

def show(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request, 'show.html', context)

def update_record(request,id):
    current_url=request.path
    record=Student.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        course=request.POST.get('course')
        college=request.POST.get('college')
        idc=request.FILES.get('idc')
        mail=request.POST.get('mail')
        try:
            record.name=name
            record.mail=mail
            record.course=course
            record.college=college
            if idc:
                record.id_card=idc
            record.save()
            return redirect('/admin_pannel')
            messages.success(request, 'updated successfully!')
        except:
            return HttpResponse('something got wrong')
    return render(request, 'update.html', {'i':record})

def delete_record(request,id):
    current_url=request.path
    record=Student.objects.get(id=id)
    record.delete()
    messages.error(request, 'deleted successfully!')
    return redirect(current_url)
    # return (request)    

def doctor(request):
    data=Student.objects.filter(course='Doctor')
    return render(request, 'doctor.html', {'data':data})

def engineer(request):
    data=Student.objects.filter(course='Engineer')
    return render(request, 'engineer.html', {'data':data})


def user_login(request):
    if request.method=='POST':
        user=request.POST.get('username')
        password=request.POST.get('password')
        admin=authenticate(username=user, password=password)
        if admin is not None:
            print(admin)
            login(request, admin)
            return redirect('/admin_pannel')
        else:
            messages.error(request, 'something is wrong!')
    return render(request, 'login.html')

def user_register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        new_user=User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
        if new_user is not None:
            new_user.save()
            messages.success(request, 'New User Registered Successfully!')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    return redirect('/login')

def SendMail(request,id):
    record=Student.objects.get(id=id)
    if request.method=='POST':
        sub=request.POST.get('subject')
        mess=request.POST.get('message')
        cc=[request.POST.get('cc')]
        bcc=[request.POST.get('bcc')]
        to=[record.mail]
        files = request.FILES.getlist('attachment')
        try:
            mail=EmailMessage(sub, mess, cc=cc, bcc=bcc, to=to)
            for f in files:
                mail.attach(f.name, f.read(), f.content_type)
            mail.send()
            messages.success(request, 'Successfully send!')
            # return HttpResponse('send successfully!')
        except:
            messages.error(request, 'Not Send')
            # return HttpResponse('somethingggg')
    return render(request, 'mail.html')