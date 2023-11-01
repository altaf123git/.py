from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    department=models.CharField(max_length=50)
    dob=models.DateField()
    age=models.IntegerField()
    city=models.CharField(max_length=50)