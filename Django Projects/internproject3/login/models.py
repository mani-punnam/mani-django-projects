from django.db import models

# Create your models here.
class Employee(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    role=models.CharField(max_length=20)
