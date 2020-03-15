from django import forms
from secondapp.models import Student
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
