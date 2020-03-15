from django.contrib import admin

# Register your models here.
from application.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['sregno','sname','smarks','Aadhar']
admin.site.register(Student,StudentAdmin)
