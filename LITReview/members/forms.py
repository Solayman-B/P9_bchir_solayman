from django import forms
from members.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
		password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
		password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmation '
																										'du mot de '
																										'passe'}))
		fields = ['username', 'password']

def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "Erreur, les champs 'mot de passe' et 'confirmation' sont différents"
            )
#validate data pour veirifer que password1 = password2