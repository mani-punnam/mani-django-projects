from django.contrib import admin
from application.models import *
# Register your models here.
class StudentSignUpAdmin(admin.ModelAdmin):
    list_display=['sregno','password']
class EmployeeSignUpAdmin(admin.ModelAdmin):
    list_display=['empid','password']
class AdminSignUpAdmin(admin.ModelAdmin):
    list_display=['username','password']
class StudentAdmin(admin.ModelAdmin):
    list_display=['sregno','sname','gender','email','sper']
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddress']
admin.site.register(StudentSignUp,StudentSignUpAdmin)
admin.site.register(EmployeeSignUp,EmployeeSignUpAdmin)
admin.site.register(AdminSignUp,AdminSignUpAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
