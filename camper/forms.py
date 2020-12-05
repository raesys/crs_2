from django import forms
from .models import Camper

class CamperForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget = forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    class Meta:
        model = Camper
        fields = ['first_name', 'last_name','gender','date_of_birth','email','phone','different_class',]

    def __init__(self, *args, **kwargs):
        super(CamperForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = 'Select'
        self.fields['different_class'].empty_label = 'Select'
        

