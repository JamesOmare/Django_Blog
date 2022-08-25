from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

"""
    UserRegistration
    username
    email
    password
    confirm_pass

    LoginForm
    username
    password
"""

# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegistrationForm(UserCreationForm):
    """Form definition for UserRegistration."""

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Your Username'
        self.fields['username'].widget=forms.TextInput(attrs={'class': 'form-control'})

        self.fields['email'].label = 'Your Email'
        self.fields['email'].widget=forms.TextInput(attrs={'class': 'form-control'})

        self.fields['password1'].label = 'Your Password'
        self.fields['password1'].widget=forms.PasswordInput(attrs={'class': 'form-control'})

        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].widget=forms.PasswordInput(attrs={'class': 'form-control'})

    class Meta:
        """Meta definition for UserRegistrationform."""

        model = User
        fields = ('username', 'email', 'password1', 'password2')

