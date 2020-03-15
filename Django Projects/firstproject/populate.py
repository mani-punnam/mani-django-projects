import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')
django.setup()
from faker import Faker
from firstapp.models import Employee,Student
fake=Faker()
s=input("Which table do you want i.e. Employee or student")
if(s=="Employee"):
    for i in range(int(input("How many records do you want"))):
        eno=fake.random_number(2)
        ename=fake.name()
        esal=fake.random_int(min=1000,max=100000)
        get=Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal)
elif(s=="Student"):
    l=[]
    for i in range(int(input("How manay records do you want"))):
        sregno=fake.random_number(2)
        sname=fake.name()
        smarks=fake.random_int(min=10000,max=100000)
        Student.objects.get_or_create(sregno=sregno,sname=sname,smarks=smarks)
