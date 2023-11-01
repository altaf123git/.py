from django.db import models
from django.contrib.auth.models import AbstractUser

#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    mail=models.CharField(max_length=50, default='abc@gmail.com')
    id_card=models.FileField(upload_to='id_photo')
    
# class CustomUser(AbstractUser):
#     phone=models.CharField(max_length=50)