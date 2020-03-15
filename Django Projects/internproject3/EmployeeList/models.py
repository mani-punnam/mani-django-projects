from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.CharField(max_length=40)
    MobileNo=models.IntegerField()
    Address=models.CharField(max_length=500)

    class Meta:
        abstract = True

class CEO(CommonInfo):
    class Meta:
        ordering=['username']
class HR(CommonInfo):
    Senior=models.ForeignKey(CEO,on_delete=models.CASCADE,related_name='hrs')
    class Meta:
        ordering=['username']
class ProjectManager(CommonInfo):
    Senior=models.ForeignKey(HR,on_delete=models.CASCADE,related_name='project_managers')
    class Meta:
        ordering=['username']
class TeamLead(CommonInfo):
    Senior=models.ForeignKey(ProjectManager,on_delete=models.CASCADE,related_name='team_leads')
    class Meta:
        ordering=['username']
class TeamMember(CommonInfo):
    Senior=models.ForeignKey(TeamLead,on_delete=models.CASCADE,related_name='team_members')
    class Meta:
        ordering=['username']
class PendingUpdate(CommonInfo):
    class Meta:
        ordering=['username']
