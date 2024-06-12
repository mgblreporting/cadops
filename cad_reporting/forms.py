from crispy_forms.helper import FormHelper
from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        help_text='Enter your username',
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        help_text='Enter your password',
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )