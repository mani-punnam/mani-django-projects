from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-eno')
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esal')
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    objects=CustomManager()
class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
class ProxyEmployee2(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True
class Student(models.Model):
    sregno=models.IntegerField()
    sname=models.CharField(max_length=30)
    smarks=models.IntegerField()
    #objects=CustomManager2()
