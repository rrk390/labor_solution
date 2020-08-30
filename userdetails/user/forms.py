from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password')

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Your Email ID'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter Your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Your last name'}),
        }


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('profile_pic',)