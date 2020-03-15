from django import forms
from django.core import validators
def name_validate(value):
    if(not value.startswith('m')):
        raise forms.ValidationError('Name must be started with m')
class StudentRegistration(forms.Form):
    sregno=forms.IntegerField()
    sname=forms.CharField(validators=[name_validate])
    smarks=forms.IntegerField()
    saddress=forms.CharField(widget=forms.Textarea)
    spassword=forms.CharField(widget=forms.PasswordInput)
    srpassword=forms.CharField(widget=forms.PasswordInput)
    #def clean_sname(self):
    #    inputname=self.cleaned_data['sname']
    #    print(self.cleaned_data['sregno'])
    #    if(len(inputname)<5):
    #        raise forms.ValidationError('Length should be greater than 4')
    #    return inputname
    #def clean_smarks(self):
    #    inputmarks=self.cleaned_data['smarks']
    #    if(inputmarks<35):
    #        raise forms.ValidationError('sorry, you are failed')
    #    return inputmarks
    def clean(self):
        #cleaned_data=super().clean()
        #rno=cleaned_data['sregno']
        rno=self.cleaned_data['sregno']
        if(rno<-1):
            raise forms.ValidationError('Hello boss Please provide valid number')
