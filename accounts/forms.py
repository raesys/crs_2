from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'district', 'local_church']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['district'].empty_label = 'Select'



class AddFundsForm(forms.Form):
    mtn_momo_number = forms.CharField(max_length=10, min_length=10, label='MTN Momo Number', help_text='Your MTN Momo number without spaces')
    mtn_momo_name = forms.CharField(max_length=100, label='MTN Momo Name', help_text='The registered name on your MTN Momo')
    amount = forms.DecimalField(decimal_places=0, max_digits=4, min_value=1, max_value=1000)

    '''
    def clean_mtn_momo_number(self, *args, **kwargs):
        mtn_momo_number = self.cleaned_data.get('mtn_momo_number')
        try:
            num = int(mtn_momo_number) 
        except ValueError:
            num = None

        # if not isinstance(mtn_momo_number, int):
        if num is None:
            raise forms.ValidationError("This is not a valid phone number.")
        if not mtn_momo_number.startswith('0'):
            raise forms.ValidationError("This is not a valid phone number.")
        return mtn_momo_number
    '''

