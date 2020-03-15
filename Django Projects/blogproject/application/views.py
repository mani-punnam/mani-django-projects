from django.shortcuts import render

# Create your views here.
def start_view(request):
    return render(request,'application/start.html')
def sample_view(request,a,b):
    print(a,b)
    return render(request,'application/sample.html')
