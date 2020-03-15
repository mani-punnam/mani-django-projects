from django.shortcuts import render

# Create your views here.
def view(request):
    count=request.session.get('count',0)+1
    request.session['count']=count
    del request.session['count']
    return render(request,'fourthapp/sample.html',{'count':count})
