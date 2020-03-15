from django.shortcuts import render

# Create your views here.
def view(request):
    #count=int(request.COOKIES.get('count',0))+1
    #response=render(request,'thirdapp/sample.html',{'count':count})
    #response.set_cookie('count',count,max_age=60)
    count=request.session.get('count',0) + 1
    request.session['count']=count
    a=request.session.get_expiry_date()
    b=request.session.get_expiry_age()
    return render(request,'thirdapp/sample.html',{'count':count,'date':a,'age':b})
