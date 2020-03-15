from django.shortcuts import render

# Create your views here.
def sample_view(request):
    return render(request,'application/sample.html')
