from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email',)

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('faculty', 'grade')