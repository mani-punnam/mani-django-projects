#from django.shortcuts import render
from django.db.models import *
from django.views.generic import *
from django.http import HttpResponse
from application.models import *
from django.urls import reverse_lazy
# Create your views here.
class SampleView(View):
    def get(self,request):
        return HttpResponse('<h1>Hello , this is from class based view</h1>')
class SampleTemplateView(TemplateView):
    template_name="application/sample.html"
class InfoView(TemplateView):
    template_name="application/info.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='manikanta'
        context['age']=22
        context['course']='MCA'
        context['register_number']=12
        return context
class BooksList(ListView):
    model=Book
    template_name="application/book_list.html"  # default one is also book_list.html --------->  modelname_list.html
    context_object_name="books"                  # default one is book_list --------> modelname_list
class BooksDetail(DetailView):
    model=Book
    template_name="application/book_detail.html" #default one is also same like this
    context_object_name="book"
class BooksCreate(CreateView):
    model=Book
    fields=['title','author','no_of_pages','price']
class BooksUpdate(UpdateView):
    model=Book
    fields=('no_of_pages','price')
class BooksDelete(DeleteView):
    model=Book
    success_url=reverse_lazy('home')
def test_view(request):
    #ct=Book.objects.all().aggregate(Count('title'))
    #max=Book.objects.all().aggregate(Max('price'))
    #min=Book.objects.all().aggregate(Min('price'))
    #avg=Book.objects.all().aggregate(Avg('price'))
    #b1=Book(title='mahaabarath',author='rudra',no_of_pages=50,price=100)
    #b2=Book(title='PHP',author='stephen',no_of_pages=30,price=200)
    #Book.objects.bulk_create([b1,b2])
    return HttpResponse('ok , good')
