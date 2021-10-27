from django.contrib.auth import authenticate, login
from django.shortcuts import render
from LITReview import forms
from LITReview.forms import authentification_form


def index(request):
	login_form = forms.authentification_form()
	message = ''
	if request.method == 'POST':
		print(request.POST)
		login_form = forms.authentification_form(request.POST)
		if login_form.is_valid():
			print('hello1')
			user = authenticate(
				username=login_form.cleaned_data['username'],
				password=login_form.cleaned_data['password1'],
			)
			print(user)
			if user is not None:
				login(request, user)
				message = 'connexion réussie'
			else:
				message = 'Erreur saisie invalide'
	return render(
		request, 'members/index.html', context={'form': login_form, 'message': message}
	)

def inscription(request):
	inscription_form = authentification_form(request.POST)
	context = {'form':inscription_form}
	return render(request, "members/inscription.html", context)