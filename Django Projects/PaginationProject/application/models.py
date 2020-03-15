from django.db import models

# Create your models here.
class Student(models.Model):
    sregno=models.IntegerField()
    sname=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    smarks=models.IntegerField()
