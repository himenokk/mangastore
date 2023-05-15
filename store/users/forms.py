from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter your name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter your surname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Choose a username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Choose a password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
