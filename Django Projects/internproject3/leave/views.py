from django.shortcuts import render,redirect
from EmployeeList.models import TeamMember,TeamLead,ProjectManager,HR,CEO,PendingUpdate
from login.models import Employee
from leave.models import LeaveManagement,Pending,Applied,Cancelled
from django.views.decorators.cache import cache_control
from django.core.mail import EmailMultiAlternatives,send_mail
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def check_session_view(request):
    if(request.session.get('eun',0)):
        data={'function_name':'check_session','is_success':'success'}
    else:
        data={'function_name':'check_session','is_success':'failure'}
    return JsonResponse(data)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_view(request,un):
    if(request.session.get('eun',0)):
        qs=LeaveManagement.objects.get(username=un)
        applied,pending,pl=qs.applied,qs.pending,qs.paidleaves
        if(qs.applied>12):
            remainder=0
        else:
            remainder=12-applied
        role=Employee.objects.get(username=un).role
        username=[]
        if(role=='HR'):
            hr=''
            pm=ProjectManager.objects.filter(Senior__username=un)
            tl=TeamLead.objects.filter(Senior__Senior__username=un)
            tm=TeamMember.objects.filter(Senior__Senior__Senior__username=un)
            for obj in pm:
                username.append(obj.username)
            for obj in tl:
                username.append(obj.username)
            for obj in tm:
                username.append(obj.username)
            applied_leaves=Applied.objects.filter(username__in=username)
            qs=HR.objects.get(username=un)
        elif(role=='ProjectManager'):
            hr,pm,tl,tm,applied_leaves='','','','',''
            qs=ProjectManager.objects.get(username=un)
        elif(role=='TeamLead'):
            hr,pm,tl,tm,applied_leaves='','','','',''
            qs=TeamLead.objects.get(username=un)
        elif(role=='TeamMember'):
            hr,pm,tl,tm,applied_leaves='','','','',''
            qs=TeamMember.objects.get(username=un)
        elif(role=='CEO'):
            hr=HR.objects.filter(Senior__username=un)
            pm=ProjectManager.objects.filter(Senior__Senior__username=un)
            tl=TeamLead.objects.filter(Senior__Senior__Senior__username=un)
            tm=TeamMember.objects.filter(Senior__Senior__Senior__Senior__username=un)
            for obj in hr:
                username.append(obj.username)
            for obj in pm:
                username.append(obj.username)
            for obj in tl:
                username.append(obj.username)
            for obj in tm:
                username.append(obj.username)
            applied_leaves=Applied.objects.filter(username__in=username)
            qs=CEO.objects.get(username=un)
        return render(request,'leave/home.html',{'un':un,'applied':applied,'remainder':remainder,'pending':pending,'pl':pl,'qs':qs,'role':role,'hr':hr,'pm':pm,'tl':tl,'tm':tm,'applied_leaves':applied_leaves})
    else:
        return redirect('/login/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def apply_for_leave_view(request):
    if(request.session.get('eun',0)):
        flag=0
        un=request.session.get('eun')
        if(request.method=="POST"):
            qs=LeaveManagement.objects.get(username=un)
            qs.pending=qs.pending + 1
            dt=datetime.now().strftime("%d-%m-%Y %H:%M:%S:%f")
            qs2=Pending(username=un,date_and_time=dt,days=request.POST['days'],description=request.POST['dsrp'])
            url=request.build_absolute_uri('/leave/approval/'+un+'/'+request.POST['days']+'/'+dt+'/')
            subject='LEAVE LETTER FROM '+un.upper()
            text_content='Important message'
            html_content = '<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"></head><body><h1>'+un.upper()+' wants to take the leave for '+request.POST['days']+' days</h1><strong>Description:</strong><p>'+request.POST['dsrp']+'</p><a class="btn btn-primary" href="'+url+'">Aprrove here</a></body></html>'
            query_object=Employee.objects.get(username=un)
            role=query_object.role
            #hr=HR.objects.filter(project_managers__team_leads__team_members__username=un)[0]
            #email=hr.Email
            if(role=='TeamMember'):
                tl=TeamLead.objects.filter(team_members__username=un)[0]
                email=tl.Email
            elif(role=='TeamLead'):
                pm=ProjectManager.objects.filter(team_leads__username=un)[0]
                email=pm.Email
            elif(role=='ProjectManager'):
                hr=HR.objects.filter(project_managers__username=un)[0]
                email=hr.Email
            elif(role=='HR'):
                ceo=CEO.objects.filter(hrs__username=un)[0]
                email=ceo.Email
            msg = EmailMultiAlternatives(subject, text_content,un.upper(), [email])
            msg.attach_alternative(html_content, "text/html")
            if(msg.send()):
                flag=1
                qs.save()
                qs2.save()
            else:
                flag=-1
        return render(request,'leave/apply_for_leave.html',{'flag':flag,'un':un})
    else:
        return redirect('/login/login')
def approval_view(request,un,days,dt):
    if(Pending.objects.filter(username=un,date_and_time=dt).exists()):
        exists='exist'
    elif(Cancelled.objects.filter(username=un,date_and_time=dt).exists()):
        exists='cancelled'
    else:
        exists='approved'
    return render(request,'leave/approval.html',{'un':un,'days':days,'dt':dt,'exists':exists})
def approval_test_view(request):
    if(Pending.objects.filter(username=request.POST['un'],date_and_time=request.POST['dt']).exists()):
        action=request.POST['action']
        if(action=='yes'):
            un=request.POST['un']
            days=request.POST['days']
            dt=request.POST['dt']
            p=Pending.objects.get(username=un,date_and_time=dt)
            qs=Employee.objects.get(username=un)
            email=qs.email
            role=qs.role
            dsrp=p.description
            aprt=datetime.now().strftime("%d-%m-%Y %H:%M:%S:%f")
            a=Applied(username=un,applied_time=dt,approved_time=aprt,days=int(days),description=dsrp)
            qs=LeaveManagement.objects.get(username=un)
            qs.applied=qs.applied + int(days)
            qs.pending = qs.pending - 1
            if(qs.applied > 12):
                qs.paidleaves = qs.applied - 12
            if(role=='TeamMember'):
                hr=HR.objects.filter(project_managers__team_leads__team_members__username=un)[0]
                tl=TeamLead.objects.filter(team_members__username=un)[0]
                senior='TeamLead('+tl.username.upper()+')'
            elif(role=='TeamLead'):
                hr=HR.objects.filter(project_managers__team_leads__username=un)[0]
                pm=ProjectManager.objects.filter(team_leads__username=un)[0]
                senior='ProjectManager('+pm.username.upper()+')'
            elif(role=='ProjectManager'):
                hr=HR.objects.filter(project_managers__username=un)[0]
                senior='HR('+hr.username.upper()+')'
            elif(role=='HR'):
                ceo=CEO.objects.filter(hrs__username=un)[0]
                senior='CEO('+ceo.username.upper()+')'
            send=send_mail('APPROVAL LETTER FROM YOUR '+senior,'You are eligible to take leave for '+str(days)+' days','HR',[email])
            if(send):
                data={'is_success':'success'}
                qs.save()
                p.delete()
                a.save()
                if(role=='TeamMember'):
                    email=hr.Email
                    send_mail('LEAVE LETTER CONFIRMATION','LEAVE LETTER FROM TeamMember('+un.upper()+') has been approved by '+senior,senior,[email])
                elif(role=='TeamLead'):
                    email=hr.Email
                    send_mail('LEAVE LETTER CONFIRMATION','LEAVE LETTER FROM TeamLead('+un.upper()+') has been approved by '+senior,senior,[email])
            else:
                data={'is_success':'no'}
        else:
            un=request.POST['un']
            days=request.POST['days']
            dt=request.POST['dt']
            p=Pending.objects.get(username=un,date_and_time=dt)
            qs=Employee.objects.get(username=un)
            email=qs.email
            qs=LeaveManagement.objects.get(username=un)
            qs.pending = qs.pending - 1
            role=Employee.objects.get(username=un).role
            if(role=='TeamMember'):
                senior='TeamLead('+TeamLead.objects.filter(team_members__username=un)[0].username.upper()+')'
            elif(role=='TeamLead'):
                senior='ProjectManager('+ProjectManager.objects.filter(team_leads__username=un)[0].username.upper()+')'
            elif(role=='ProjectManager'):
                senior='HR('+HR.objects.filter(project_managers__username=un)[0].username.upper()+')'
            elif(role=="HR"):
                senior='CEO('+CEO.objects.filter(hrs__username=un)[0].username.upper()+')'
            send=send_mail('APPROVAL LETTER FROM Your '+senior,'You are not eligible to take leave for '+str(days)+' days','HR',[email])
            if(send):
                data={'is_success':'success'}
                qs.save()
                p.delete()
            else:
                data={'is_success':'no'}
    elif(Cancelled.objects.filter(username=request.POST['un'],date_and_time=request.POST['dt']).exists()):
        data={'is_success':'cancelled'}
    else:
        data={'is_success':'approved'}
    return JsonResponse(data)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def applied_view(request):
    un=request.session.get('eun',0)
    if(un):
        applied=Applied.objects.filter(username=un)
    else:
        return redirect('/login/login')
    return render(request,'leave/applied.html',{'applied':applied})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pending_view(request):
    un=request.session.get('eun',0)
    if(un):
        pending=Pending.objects.filter(username=un)
    else:
        return redirect('/login/login')
    return render(request,'leave/pending.html',{'pending':pending})
def cancel_view(request):
    id=int(request.POST['id'])
    if(Pending.objects.filter(id=id).exists()):
        qs=Pending.objects.get(id=id)
        un=qs.username
        dt=qs.date_and_time
        Cancelled.objects.create(username=un,date_and_time=dt)
        qs.delete()
        qs=LeaveManagement.objects.get(username=un)
        qs.pending = qs.pending - 1
        qs.save()
        data={'is_delete':'success'}
    else:
        data={'is_delete':'already'}
    return JsonResponse(data)
def update_view(request):
    un=request.POST['un']
    fn,ln,email,mbno,address=request.POST['fn'],request.POST['ln'],request.POST['email'],int(request.POST['mbno']),request.POST['address']
    role=Employee.objects.get(username=un).role
    if(role=='CEO' or role=='HR'):
        if(role=='CEO'):
            qs=CEO.objects.get(username=un)
        else:
            qs=HR.objects.get(username=un)
        qs.FirstName,qs.LastName,qs.Email,qs.MobileNo,qs.Address=fn,ln,email,mbno,address
        qs.save()
        qs=Employee.objects.get(username=un)
        qs.email=email
        qs.save()
        data={'function_name':'update','is_success':'success'}
    else:
        url=request.build_absolute_uri('/leave/confirm_update/'+un)
        subject='INFORMATION UPDATE MESSAGE FROM '+un.upper()
        text_content='update info message'
        message=request.POST['message'].rstrip(',')
        html_content = '<h1>'+un.upper()+' wants to change the '+message+'</h1><a href="'+url+'">Approve here</a>'
        if(role=='TeamMember'):
            hr=HR.objects.filter(project_managers__team_leads__team_members__username=un)[0]
        elif(role=='TeamLead'):
            hr=HR.objects.filter(project_managers__team_leads__username=un)[0]
        elif(role=='ProjectManager'):
            hr=HR.objects.filter(project_managers__username=un)[0]
        hr_email=hr.Email
        msg = EmailMultiAlternatives(subject, text_content,un.upper(), [hr_email])
        msg.attach_alternative(html_content, "text/html")
        pu=PendingUpdate(username=un,FirstName=fn,LastName=ln,Email=email,MobileNo=mbno,Address=address)
        if(msg.send()):
            pu.save()
            data={'function_name':'update','is_success':'pending'}
        else:
            data={'function_name':'update','is_success':'failure'}
    return JsonResponse(data)
def confirm_update_view(request,un):
    if(PendingUpdate.objects.filter(username=un).exists()):
        exists=1
    else:
        exists=-1
    return render(request,'leave/confirm_update.html',{'un':un,'exists':exists})
def confirm_update_test_view(request):
    un=request.POST['un']
    if(PendingUpdate.objects.filter(username=un).exists()):
        action=request.POST['action']
        pu=PendingUpdate.objects.get(username=un)
        emp=Employee.objects.get(username=un)
        role=emp.role
        email=emp.email
        if(action=='yes'):
            if(role=="ProjectManager"):
                qs=ProjectManager.objects.get(username=un)
            elif(role=="TeamLead"):
                qs=TeamLead.objects.get(username=un)
            elif(role=="TeamMember"):
                qs=TeamMember.objects.get(username=un)
            qs.FirstName,qs.LastName,qs.Email,qs.MobileNo,qs.Address=pu.FirstName,pu.LastName,pu.Email,pu.MobileNo,pu.Address
            emp.email=pu.Email
            send=send_mail('Update Confirmation from HR','Congrats!, your data has been successfully updated','HR',[email])
            if(send):
                qs.save()
                emp.save()
                pu.delete()
                data={'is_success':'success'}
            else:
                data={'is_success':'no'}
        else:
            send=send_mail('Update Confirmation from HR','Sorry you can not update your data right now, try again other time','HR',[email])
            if(send):
                pu.delete()
                data={'is_success':'success'}
            else:
                data={'is_success':'no'}
    else:
        data={'is_success':'already'}
    return JsonResponse(data)
