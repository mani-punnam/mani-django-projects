from django.contrib import admin
# Register your models here.\

#LogIn Application
from login.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['username','password','email','role']

admin.site.register(Employee,EmployeeAdmin)

#Leave Application
from leave.models import LeaveManagement,Pending,Applied,Cancelled

class LeaveManagementAdmin(admin.ModelAdmin):
    list_display=['username','applied','pending','paidleaves']
class PendingAdmin(admin.ModelAdmin):
    list_display=['username','date_and_time','days','description']
class AppliedAdmin(admin.ModelAdmin):
    list_display=['username','applied_time','approved_time','days','description']
class CancelledAdmin(admin.ModelAdmin):
    list_display=['username','date_and_time']
admin.site.register(LeaveManagement,LeaveManagementAdmin)
admin.site.register(Pending,PendingAdmin)
admin.site.register(Applied,AppliedAdmin)
admin.site.register(Cancelled,CancelledAdmin)

#EmployeeList Application
from EmployeeList.models import CEO,HR,ProjectManager,TeamLead,TeamMember,PendingUpdate

class CEOAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','MobileNo','Address']
class HRAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','MobileNo','Address','Senior']
class ProjectManagerAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','MobileNo','Address','Senior']
class TeamLeadAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','MobileNo','Address','Senior']
class TeamMemberAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','MobileNo','Address','Senior']
class PendingUpdateAdmin(admin.ModelAdmin):
    list_display=['username','FirstName','LastName','Email','MobileNo','Address']

admin.site.register(CEO,CEOAdmin)
admin.site.register(HR,HRAdmin)
admin.site.register(ProjectManager,ProjectManagerAdmin)
admin.site.register(TeamLead,TeamLeadAdmin)
admin.site.register(TeamMember,TeamMemberAdmin)
admin.site.register(PendingUpdate,PendingUpdateAdmin)
