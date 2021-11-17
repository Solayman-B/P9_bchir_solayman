from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))


class UserForm(UserCreationForm):
	username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))
	password2 = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput(attrs={'placeholder': "Confirmation"}))

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']