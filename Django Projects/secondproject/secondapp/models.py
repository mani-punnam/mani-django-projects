from django.db import models

# Create your models here.
class Student(models.Model):
    sregno=models.IntegerField()
    sname=models.CharField(max_length=30)
    smarks=models.IntegerField()
