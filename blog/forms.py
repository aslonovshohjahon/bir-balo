from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True ,widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    password = forms.CharField(label = 'Passwod1',required=True , widget=forms.PasswordInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    password2 = forms.CharField(label = 'Password2', required=True, widget=forms.PasswordInput(attrs={'class': 'from-control footer-input margin-b-20'}))
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control footer-imput margin-b-20'}))
    firs_name = forms.CharField(label='First name', required=True, widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control footer-input margin-b-20'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )