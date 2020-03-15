from django.shortcuts import render
from firstapp.models import Employee,Student
from django.db.models import Q
from . import forms
# Create your views here.
def view1(request):
    #employee=Employee.objects.filter(ename='Joanna Holmes')|Employee.objects.filter(eno=111)
    #employee=Employee.objects.filter(pk=2)[0]   #It won't work as i have written for loop in html file.
    #employee=Employee.objects.filter(pk=2)[0:1]   #But it will work
    #employee=Employee.objects.filter(ename__contains='ab')  #it means like '%ab%'
    #employee=Employee.objects.filter(Q(pk__in=[1,2,3]),Q(eno=111) | Q(ename='Joanna Holmes')).delete()
    employee=Employee.objects.filter(ename__contains='ab').update(ename='manikanta',eno=9999)
    employee=Employee.objects.filter(eno=9999)
    return render(request,'firstapp/sample.html',{'employee':employee})
def view2(request):
    form=forms.StudentRegistration()
    #student=Student.objects.all()
    if(request.method=="POST"):
        form=forms.StudentRegistration(request.POST)
        if(form.is_valid()):
            return render(request,'firstapp/sample4.html',{'student':form.cleaned_data})
    return render(request,'firstapp/sample3.html',{'form':form})
