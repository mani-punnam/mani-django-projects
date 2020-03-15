from application.models import Sample
from django import forms
class Sample(forms.ModelForm):
    class Meta:
        model=Sample
        fields='__all__'
