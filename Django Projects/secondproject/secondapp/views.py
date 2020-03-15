from django.shortcuts import render,redirect
from . import forms
from secondapp.models import Student
# Create your views here.
def view(request):
    form=forms.StudentRegistration()
    if(request.method=="POST"):
        form=forms.StudentRegistration(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            student=Student.objects.all()
            return render(request,'secondapp/result.html',{'student':student})
    return render(request,'secondapp/index.html',{'form':form})
def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/table')
def table_view(request):
    student=Student.objects.all()
    return render(request,'secondapp/result.html',{'student':student})
def update_view(request,id):
    std=Student.objects.get(id=id)
    if(request.method=="POST"):
        form=forms.StudentRegistration(request.POST,instance=std)
        if(form.is_valid()):
            form.save()
            return redirect('/table')
    form=forms.StudentRegistration(instance=std)
    return render(request,'secondapp/update.html',{'form':form})
