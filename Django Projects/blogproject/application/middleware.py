from django.http import HttpResponse
class CustomMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("Execution before processing the request")
        response=self.get_response(request)
        print("Execution after processing the request")
        return response
    def process_exception(self,request,exception):
        s1=str(exception.__class__.__name__)
        s2=str(exception)
        return HttpResponse(s1+" one "+s2)
class SecondMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("before")
        response=self.get_response(request)
        print("after")
        return response
    def process_exception(self,request,exception):
        return HttpResponse(str(exception.__class__.__name__)+" two "+str(exception))
