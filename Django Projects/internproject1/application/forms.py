from django import forms
from application.models import *

class StudentSignUp(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=StudentSignUp
        fields=['sregno','password']
class EmployeeSignUp(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=EmployeeSignUp
        fields=['empid','password']
class AdminSignUp(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AdminSignUp
        fields=['username','password']
class Student(forms.ModelForm):
    choices=[('MALE','male'),('FEMALE','female')]
    gender=forms.CharField(max_length=10,widget=forms.Select(choices=choices))
    class Meta:
        model=Student
        fields=['sregno','sname','gender','email','sper']
class Employee(forms.ModelForm):
    eaddress=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Employee
        fields=['eno','ename','esal','eaddress']
