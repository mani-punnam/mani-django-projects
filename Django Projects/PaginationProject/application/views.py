from django.shortcuts import render
from django.views.generic import ListView
from application.models import Student
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
class StudentListView(ListView):
    model=Student
    paginate_by=2
def student_view(request):
    student_list=Student.objects.all()
    paginator=Paginator(student_list,2)
    page_number=request.GET.get('page')
    try:
        student_list=paginator.page(page_number)
    except PageNotAnInteger:
        student_list=paginator.page(1)
    except EmptyPage:
        student_list=paginator.page(paginator.num_pages)
    return render(request,'application/student_list2.html',{'student_list':student_list})
def sample_view(request):
    return render(request,'application/sample.html')
def email_view(request):
    url=request.build_absolute_uri('/sample')
    send=send_mail('URL BUILDING',url,'manikanta punnam\'s',['punnammani@gmail.com'])
    if(send):
        return HttpResponse('Success')
    else:
        return HttpResponse('Failure')
