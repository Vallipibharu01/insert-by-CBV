from django import forms
from app.models import *

class SchoolForm(forms.ModelForm):
    class Meta():
        model=school
        fields='__all__'



