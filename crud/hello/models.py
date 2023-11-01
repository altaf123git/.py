from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    dob= models.DateField()
    adhaar=models.FileField(upload_to='adhaar')