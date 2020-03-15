from django.shortcuts import render,redirect
from login.models import Employee
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse

# Create your views here.
def login_view(request):
    if(request.session.get('eun',0)):
        return redirect('/leave/home/'+request.session.get('eun'))
    else:
        error=0
        if(request.method=="POST"):
            un=request.POST['username']
            if(Employee.objects.filter(username=un).exists()):
                qs=Employee.objects.get(username=un)
                psd=request.POST['password']
                if(psd==qs.password):
                    request.session['eun']=un
                    return redirect('/leave/home/'+un)
                else:
                    error=1
            else:
                error=1
        return render(request,'login/login.html',{'error':error})
def change_password_view(request):
    return render(request,'login/change_password.html')
def change_password_test_view(request):
    un=request.POST['un']
    if(Employee.objects.filter(username=un).exists()):
        qs=Employee.objects.get(username=un)
        email=qs.email
        url=request.build_absolute_uri('/login/confirm_password/'+un+'/')
        html_content='<p>you can change your password <a href="'+url+'">here</a></p>'
        msg = EmailMultiAlternatives('CHANGE YOUR PASSWORD','To change the password',un.upper(), [email])
        msg.attach_alternative(html_content, "text/html")
        if(msg.send()):
            data={'is_success':'success'}
        else:
            data={'is_success':'failure'}
    else:
        data={'is_success':'not_exist'}
    return JsonResponse(data)
def confirm_password_view(request,un):
    return render(request,'login/confirm_password.html',{'un':un})
def confirm_password_test_view(request):
    un=request.POST['un']
    password=request.POST['password']
    qs=Employee.objects.get(username=un)
    qs.password=password
    qs.save()
    data={'is_success':'success'}
    return JsonResponse(data)
def logout_view(request):
    request.session.flush()
    #del request.session['eun']
    return redirect('/login/login')
