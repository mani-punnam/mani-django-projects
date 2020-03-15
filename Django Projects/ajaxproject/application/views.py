from django.shortcuts import render
from . import forms
from application.models import Sample
from django.http import JsonResponse
#from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
def sample_view(request):
    form=forms.Sample()
    return render(request,'application/sample.html',{'form':form})
#@ensure_csrf_cookie
def test_view(request):
    form=forms.Sample(request.POST)
    if(form.is_valid()):
        form.save()
    data={'is_taken':'success'}
    return JsonResponse(data)
def sample_view2(request):
    return render(request,'application/sample2.html')
def test_view2(request):
    name=request.POST['name']
    city=request.POST['city']
    return JsonResponse("{'name':"+name+",'city':"+city+"}",safe=False)
