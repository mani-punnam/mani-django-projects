from django.db import models

# Create your models here.
class StudentSignUp(models.Model):
    sregno=models.IntegerField()
    password=models.CharField(max_length=20)
class EmployeeSignUp(models.Model):
    empid=models.IntegerField()
    password=models.CharField(max_length=20)
class AdminSignUp(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Student(models.Model):
    choices=[('MALE','male'),('FEMALE','female')]
    sregno=models.IntegerField()
    sname=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,choices=choices)
    email=models.EmailField()
    sper=models.IntegerField()
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddress=models.TextField()
