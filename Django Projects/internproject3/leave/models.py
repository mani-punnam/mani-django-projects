from django.db import models

# Create your models here.

class LeaveManagement(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    applied=models.IntegerField()
    pending=models.IntegerField()
    paidleaves=models.IntegerField()
class Pending(models.Model):
    username=models.CharField(max_length=20)
    date_and_time=models.CharField(max_length=50)
    days=models.IntegerField()
    description=models.CharField(max_length=500)
class Applied(models.Model):
    username=models.CharField(max_length=20)
    applied_time=models.CharField(max_length=50)
    approved_time=models.CharField(max_length=50)
    days=models.IntegerField()
    description=models.CharField(max_length=500)
class Cancelled(models.Model):
    username=models.CharField(max_length=20)
    date_and_time=models.CharField(max_length=20)
