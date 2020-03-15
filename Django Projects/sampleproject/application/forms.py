from application.models import Student
from django import forms


class Student(forms.ModelForm):
    sregno=forms.IntegerField(label='Student Registration Number')
    sname=forms.CharField(label='Student Name')
    smarks=forms.IntegerField(label='Student Marks')
    Aadhar=forms.FileField(label='Aadhar File')
    class Meta:
        model=Student
        fields='__all__'
