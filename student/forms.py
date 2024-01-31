from django import forms
from .models import regt

class AddForm(forms.ModelForm):
    class Meta:
        model=regt
        fields=('firstname','lastname','email','phone','password','gender')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
        }