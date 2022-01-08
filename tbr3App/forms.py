from django import forms

from .models import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'الإسم'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'رقم الهاتف'}),
            'wilaya':forms.Select(attrs={'class':'form-select form-select-md mb-3','id':'sel '})
        }