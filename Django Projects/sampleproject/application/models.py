from django.db import models

# Create your models here.
class Student(models.Model):
    sregno=models.IntegerField()
    sname=models.CharField(max_length=50)
    smarks=models.IntegerField()
    Aadhar=models.FileField()
    
