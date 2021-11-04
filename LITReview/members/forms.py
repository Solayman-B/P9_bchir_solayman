from django import forms


class UserForm(forms.Form):
	username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
	password2 = forms.CharField(label='password2',
								widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}),
								required=False)
#validate data pour veirifer que password1 = password2