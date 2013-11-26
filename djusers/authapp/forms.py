from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username","email","password"]
        widgets = {
            "password":forms.PasswordInput
        }

class SignupForm(UserForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput
    )

class LoginForm(UserForm):
    class Meta(object):
       model = User
       fields = ["username","password"]
       widgets = {
           "password":forms.PasswordInput
       }

