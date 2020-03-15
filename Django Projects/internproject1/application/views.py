from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from . import forms
from application.models import *
# Create your views here.


def index_view(request):
    return render(request,'application/index.html')
def signup_view(request):
    return render(request,'application/signup.html')
def admin_signup_view(request):
    error=''
    if(request.method=="POST"):
        un=request.POST['username']
        form=forms.AdminSignUp(request.POST)
        try:
            a=AdminSignUp.objects.get(username=un)
            error='username already existed'
            return render(request,'application/admin_signup.html',{'form':form,'error':error})
        except:
            if(form.is_valid()):
                form.save()
                return redirect('/admin_login')
    form=forms.AdminSignUp()
    return render(request,'application/admin_signup.html',{'form':form,'error':error})
def student_signup_view(request):
    error=''
    if(request.method=="POST"):
        sno=int(request.POST['sregno'])
        form=forms.StudentSignUp(request.POST)
        a=StudentSignUp.objects.filter(sregno=sno)
        if(a):
            error='Student ID already existed'
            return render(request,'application/student_signup.html',{'form':form,'error':error})
        else:
            if(form.is_valid()):
                form.save()
                return redirect('/student_login')
    form=forms.StudentSignUp()
    return render(request,'application/student_signup.html',{'form':form,'error':error})
def employee_signup_view(request):
    error=''
    if(request.method=="POST"):
        form=forms.EmployeeSignUp(request.POST)
        eid=int(request.POST['empid'])
        a=EmployeeSignUp.objects.filter(empid=eid)
        if(a):
            error='Employee ID already existed'
            return render(request,'application/employee_signup.html',{'form':form,'error':error})
        else:
            if(form.is_valid()):
                form.save()
                return redirect('/employee_login')
    form=forms.EmployeeSignUp()
    return render(request,'application/employee_signup.html',{'form':form,'error':error})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_view(request):
    temp=request.session.get('username',0)
    if(temp):
        return render(request,'application/adm.html')
    else:
        return redirect('/admin_login')
def login_view(request):
    return render(request,'application/login.html')
def admin_login_view(request):
    if(request.session.get('username',0)):
        return redirect('/adm')
    else:
        error=""
        if(request.method=="POST"):
            un=request.POST['un']
            pwd=request.POST['pwd']
            signup=AdminSignUp.objects.all()
            for obj in signup:
                if(obj.username==un and obj.password==pwd):
                    request.session['username']=un
                    return redirect('/adm')
            error="Please enter correct username and password"
        return render(request,'application/admin_login.html',{'error':error})
def student_login_view(request):
    if(request.session.get('sid',0)):
        sid=request.session['sid']
        student=Student.objects.filter(sregno=sid)
        if(student):
            if(request.session.get('sid',0)):
                return render(request,'application/student_table.html',{'student':student})
            else:
                return redirect('/student_login')
        else:
            return redirect('/student')
    else:
        error=""
        if(request.method=="POST"):
            sid=int(request.POST['sid'])
            pwd=request.POST['pwd']
            signup=StudentSignUp.objects.all()
            for obj in signup:
                if(obj.sregno==sid and obj.password==pwd):
                    request.session['sid']=sid
                    student=Student.objects.filter(sregno=sid)
                    if(student):
                        if(request.session.get('sid',0)):
                            return render(request,'application/student_table.html',{'student':student})
                        else:
                            return redirect('/student_login')
                    else:
                        return redirect('/student')
            error="Please enter correct student ID and password"
        return render(request,'application/student_login.html',{'error':error})
def employee_login_view(request):
    if(request.session.get('eid',0)):
        eid=request.session['eid']
        employee=Employee.objects.filter(eno=eid)
        if(employee):
            if(request.session.get('eid',0)):
                return render(request,'application/employee_table.html',{'employee':employee})
            else:
                return redirect('/employee_login')
        else:
            return redirect('/employee')
    else:
        error=""
        if(request.method=="POST"):
            eid=int(request.POST['eid'])
            pwd=request.POST['pwd']
            signup=EmployeeSignUp.objects.all()
            for obj in signup:
                if(obj.empid==eid and obj.password==pwd):
                    request.session['eid']=eid
                    employee=Employee.objects.filter(eno=eid)
                    if(employee):
                        if(request.session.get('eid',0)):
                            return render(request,'application/employee_table.html',{'employee':employee})
                        else:
                            return redirect('/employee_login')
                    else:
                        return redirect('/employee')
            error="Please enter correct Employee ID and password"
        return render(request,'application/employee_login.html',{'error':error})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def student_view(request):
    if(request.session.get('sid',0)):
        error=''
        if(request.method=="POST"):
            form=forms.Student(request.POST)
            sid=int(request.POST['sregno'])
            a=Student.objects.filter(sregno=sid)
            if(a):
                error='Student ID already existed'
                return render(request,'application/student.html',{'form':form,'error':error})
            else:
                if(form.is_valid()):
                    form.save()
                    sid=int(request.POST['sregno'])
                    student=Student.objects.filter(sregno=sid)
                    return render(request,'application/student_table.html',{'student':student})
        form=forms.Student()
        return render(request,'application/student.html',{'form':form,'error':error})
    else:
        return redirect('/student_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def employee_view(request):
    if(request.session.get('eid',0)):
        error=''
        if(request.method=="POST"):
            form=forms.Employee(request.POST)
            eid=int(request.POST['eno'])
            a=Employee.objects.filter(eno=eid)
            if(a):
                error='Employee ID already existed'
                return render(request,'application/employee.html',{'form':form,'error':error})
            else:
                if(form.is_valid()):
                    form.save()
                    eno=int(request.POST['eno'])
                    employee=Employee.objects.filter(eno=eno)
                    return render(request,'application/employee_table.html',{'employee':employee})
        form=forms.Employee()
        return render(request,'application/employee.html',{'form':form,'error':error})
    else:
        return redirect('/employee_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def employee_table_view(request):
    temp = request.session.get('username',0)
    if(temp):
        employee=Employee.objects.all()
        return render(request,'application/employee_table.html',{'employee':employee})
    else:
        return redirect('/admin_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def student_table_view(request):
    temp = request.session.get('username',0)
    if(temp):
        student=Student.objects.all()
        return render(request,'application/student_table.html',{'student':student})
    else:
        return redirect('/admin_login')
def logout_view(request):
    if(request.session.get('username',0)):
        del request.session['username']
    elif(request.session.get('sid',0)):
        del request.session['sid']
    elif(request.session.get('eid',0)):
        del request.session['eid']
    return redirect('/')
