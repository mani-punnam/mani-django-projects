from django.shortcuts import render
from django.http import HttpResponse
from application.models import Article,Reporter
# Create your views here.
def sample_view(request):
    r=Reporter(first_name='prasad',last_name='punnam',email='prasad@gmail.com')
    r.save()
    a=Article(headline='python with django',pub_date='2020-01-10',reporter=r)
    a.save()
    return HttpResponse('<h1>Success</h1>')
