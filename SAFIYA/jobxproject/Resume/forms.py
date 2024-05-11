from django import forms
from Resume.models import clientDb

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = clientDb
        fields = ['resume',]