from django import forms


class authentification_form(forms.Form):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':"Nom d'utilisateur"}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe'}))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))