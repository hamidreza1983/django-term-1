from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=15)


    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput, max_length=15)
    password = forms.CharField(widget=forms.PasswordInput, max_length=15)
    confirm = forms.CharField(widget=forms.PasswordInput, max_length=15)

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, max_length=15)
    confirm = forms.CharField(widget=forms.PasswordInput, max_length=15)

class PasswordReset(forms.Form):
    email = forms.EmailField()