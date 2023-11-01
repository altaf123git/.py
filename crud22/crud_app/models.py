from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    pan=models.FileField(upload_to='pan')