from django.shortcuts import render,redirect
from application.models import Student
from . import forms
# Create your views here.


def student_view(request):
    if(request.method=="POST"):
        form=forms.Student(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
        print(request.FILES['Aadhar'])
    form=forms.Student()
    return render(request,'application/student_form.html',{'form':form,'valid':'valid','invalid':'invalid'})
