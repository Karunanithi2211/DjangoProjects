from django import forms
from .models import Registerform

class Myformcrud(forms.ModelForm):
    class Meta:
        model = Registerform
        fields= ['name','age','address', 'contact','email']