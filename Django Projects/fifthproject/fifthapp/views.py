from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fifthapp.forms import SignUp
from django.http import HttpResponseRedirect
# Create your views here.

def home_view(request):
    return render(request,'fifthapp/homepage.html')
@login_required
def java_exams_view(request):
    return render(request,'fifthapp/java_exams.html')
@login_required
def python_exams_view(request):
    return render(request,'fifthapp/python_exams.html')
@login_required
def aptitude_exams_view(request):
    return render(request,'fifthapp/aptitude_exams.html')
def logout_view(request):
    return render(request,'fifthapp/logout.html')
def signup_view(request):
    try:
        if(request.method=="POST"):
            form=SignUp(request.POST)
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        form=SignUp()
        return render(request,'fifthapp/signup.html',{'form':form})
    except ValueError:
        return render(request,'fifthapp/signup.html',{'form':form})
