from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
