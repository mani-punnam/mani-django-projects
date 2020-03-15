from django.contrib import admin
from application.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['sregno','sname','gender','email','smarks']
admin.site.register(Student,StudentAdmin)
