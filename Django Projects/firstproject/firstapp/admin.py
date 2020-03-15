from django.contrib import admin
from firstapp.models import Employee,Student,ProxyEmployee,ProxyEmployee2

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal']
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sregno','sname','smarks']
class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal']
class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)
